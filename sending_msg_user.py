import requests

TEAMNAME = "HolidaySurvivors"
MASTERSCHOOL_API_NUMBER = "491771786208"

def validate_inputs(msg, phone_num):
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
    validate_inputs(msg, phone_num)
    URL = "http://hackathons.masterschool.com:3030/sms/send"
    REQ_BODY = {
        "phoneNumber": phone_num,
        "message": msg,
        "sender": MASTERSCHOOL_API_NUMBER
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
