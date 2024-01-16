import requests, random, string, json, time, threading

url = "https://prod-api-funimationnow.dadcdigital.com/api/auth/register/"


def random(length=8):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))


def email():
    return f"{random()}@heroin.gg"


def password():
    return f"{random()}1!"


def register_account():
    A = "x-csrftoken"
    while True:
        try:
            random_email = email()
            random_password = password()
            options_headers = {
                "Access-Control-Request-Headers": "territory,x-csrftoken",
                "Access-Control-Request-Method": "POST",
                "Connection": "keep-alive",
            }
            options_response = requests.options(url, headers=options_headers)
            csrf_token = options_response.headers.get(A)
            if options_response.status_code == 200:
                headers = {
                    "devicetype": "Android Phone",
                    "User-Agent": "okhttp/3.12.1",
                    A: csrf_token,
                }
                body = {"email": random_email, "password": random_password}
                post_response = requests.post(url, headers=headers, data=body)
                if post_response.status_code == 200:
                    response_data = post_response.json()
                    user_id = response_data["user"]["id"]
                    auth_token = response_data["token"]
                    with open("login.txt", "a") as file:
                        file.write(
                            f"{random_email}:{random_password}:{user_id}:{auth_token}\n"
                        )
                    print(f"Successfully registered: {email}")
                else:
                    print(
                        f"Registration failed for {email} with status code {post_response.status_code}"
                    )
            else:
                print(
                    f"OPTIONS request failed with status code {options_response.status_code}"
                )
        except Exception as e:
            print(f"An error occurred: {e}")


num_threads = 7
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=register_account)
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()
print("Registration completed.")
