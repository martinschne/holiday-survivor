import os

import requests
from dotenv import load_dotenv

load_dotenv()
TEAMNAME = os.getenv("TEAMNAME")
MASTERSCHOOL_API_NUMBER = os.getenv("MASTERSCHOOL_API_NUMBER")


def _validate_inputs(msg, phone_num):
    # Validate msg type input
    try:
        str(msg)
    except ValueError as e:
        print("Not a valid message:" + str(e))

    # Validate phone_num input
    if not phone_num.isnumeric() or phone_num[0] == "0":
        raise ValueError("Phone Number Format not Valid!")
    else:
        try:
            int(phone_num)
        except ValueError as e:
            print("Invalid data type: " + str(e))
        except Exception as e:
            print("Not a valid phone number: " + str(e))


def sending_msg_user(msg, phone_num):
    _validate_inputs(msg, phone_num)
    sms_sending_url = "http://hackathons.masterschool.com:3030/sms/send"
    payload = {
        "phoneNumber": phone_num,
        "message": msg,
        "sender": MASTERSCHOOL_API_NUMBER
    }
    request_headers = {
        "Content-Type": "application/json"
    }
    res = requests.post(url=sms_sending_url, headers=request_headers, json=payload)
    print(f"request status code: {res.status_code}")
    if res.status_code == 200:
        print(f"Successfully sending the message to the number")
        return True
    else:
        print(f"Can not send message to the number")
        return False
