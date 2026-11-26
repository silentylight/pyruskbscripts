import json
import re
import requests

BASE_URL = "https://api.pyrus.com/v4"
TIMEOUT = 30

def load_config(path="info.json"):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def check_response(response):
    try:
        response.raise_for_status()
    except requests.HTTPError as error:
        raise requests.HTTPError(f"{error}\n{response.text}", response=response) from error

def retrieve_access_token(login, security_key):
    response = requests.post(
        f"{BASE_URL}/auth",
        json={
            "login": login,
            "security_key": security_key
        },
        timeout=TIMEOUT
    )
    check_response(response)
    return response.json()["access_token"]

def safe_filename(name):
    cleaned = re.sub(r'[\\/:*?"<>|]', "_", name).strip(" .")
    return cleaned or "saved_article"
