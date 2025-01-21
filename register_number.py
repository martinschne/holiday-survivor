import requests
from dotenv import load_dotenv
import os
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

    URL = "http://hackathons.masterschool.com:3030/team/registerNumber"
    REQ_BODY = {
        "phoneNumber": phone_num,
        "teamName": TEAMNAME
    }
    HEADERS = {
        "Content-Type": "application/json"
    }
    res = requests.post(url=URL, headers=HEADERS, json=REQ_BODY)
    print(f"request status code: {res.status_code}")
    if res.status_code == 200:
        print(f"Successfully register the number {phone_num} to team {TEAMNAME}")
        return True
    else:
        print(f"Can not register the number {phone_num} to team {TEAMNAME}")
        return False


register_new_user("49223456789")
