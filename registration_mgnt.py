import os

import requests
from dotenv import load_dotenv

load_dotenv()
TEAMNAME = os.getenv("TEAMNAME")


def validate_input(phone_num):
    """
    phone_num should be a string
    :param phone_num:
    :return:
    """
    if not phone_num.isnumeric() or phone_num[0] == "0":
        raise ValueError("Phone Number Format not Valid!")
    else:
        try:
            int(phone_num)
        except ValueError as e:
            print("Invalid data type: " + str(e))
        except Exception as e:
            print("Not a valid phone number: " + str(e))


def register_new_user(phone_num):
    # phone_num type handling
    # checking if the phone number only consists of digit
    validate_input(phone_num)

    num_registration_url = "http://hackathons.masterschool.com:3030/team/registerNumber"
    payload = {
        "phoneNumber": phone_num,
        "teamName": TEAMNAME
    }
    request_headers = {
        "Content-Type": "application/json"
    }
    res = requests.post(url=num_registration_url, headers=request_headers, json=payload)
    print(f"request status code: {res.status_code}")
    if res.status_code == 200:
        print(f"Successfully register the number {phone_num} to team {TEAMNAME}")
        return True
    else:
        print(f"Can not register the number {phone_num} to team {TEAMNAME}")
        return False


def unregister_user(phone_num):
    # validate phone number
    validate_input(phone_num)

    # Sending unregister request
    num_unregistration_url = "http://hackathons.masterschool.com:3030/team/unregisterNumber"
    payload = {
        "phoneNumber": phone_num,
        "teamName": TEAMNAME
    }
    request_headers = {
        "Content-Type": "application/json"
    }
    res = requests.post(url=num_unregistration_url, headers=request_headers, json=payload)
    print(f"request status code: {res.status_code}")
    if res.status_code == 200:
        print(f"Successfully unregister the number {phone_num} from team {TEAMNAME}")
        return True
    else:
        print(f"Can not unregister the number {phone_num} from team {TEAMNAME}")
        return False
