import random
import string
import requests

api = "https://api.easymc.io/v1/token/redeem"

def generate_random_string(length=20):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

while True:
    token = generate_random_string()
    data = {
        "token": token
    }
    r = requests.post(api, json=data)
    
    if r.status_code == 200:
        response_json = r.json()
        mc_name = response_json.get("mcName")
        uuid = response_json.get("uuid")
        session_id = response_json.get("session")
        message = response_json.get("message")
        
        print(f"Successfully redeemed token for Minecraft account:")
        print(f"  Minecraft Name: {mc_name}")
        print(f"  UUID: {uuid}")
        print(f"  Session ID: {session_id}")
        break
        if message:
            print(f"  Message: {message}")
    else:
        error_json = r.json()
        error_message = error_json.get("error")
        print(f"Error redeeming token: {error_message}")

    print(f"Token: {token}")
    print(f"Status Code: {r.status_code}")
