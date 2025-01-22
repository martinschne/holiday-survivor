import requests
from config import MASTERSCHOOL_API_PHONE_NUMBER as API_PHONE_NUM


def _validate_inputs(msg, phone_num):
    """
    Validates the inputs for sending message to user.

    :param msg: The message to be sent to the user.
    :type msg: str
    :param phone_num: The phone number of the user to receive the message.
    :type phone_num: str

    :raises ValueError: If the message is not a string or the phone number format is invalid.
    """
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
    """
    Sends a message to a user.

    :param msg: The message to be sent to the user.
    :type msg: str
    :param phone_num: The phone number of the user to receive the message.
    :type phone_num: str

    :return: True if the sending was successful, False otherwise
    :rtype: bool
    """

    _validate_inputs(msg, phone_num)
    sms_sending_url = "http://hackathons.masterschool.com:3030/sms/send"
    payload = {
        "phoneNumber": phone_num,
        "message": msg,
        "sender": API_PHONE_NUM,
    }
    request_headers = {"Content-Type": "application/json"}
    res = requests.post(
        url=sms_sending_url, headers=request_headers, json=payload
    )
    print(f"request status code: {res.status_code}")
    if res.status_code == 200:
        print("Successfully sending the message to the number")
        return True
    else:
        print("Can not send message to the number")
        return False
