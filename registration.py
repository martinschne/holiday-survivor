import requests
from config import TEAMNAME


def validate_input(phone_num: str) -> None:
    """
    Validates the phone number input.

    This function checks if the provided phone number is numeric and does not start with '0'.
    If the input is invalid, it raises a ValueError or prints an error message.

    :param phone_num: The phone number to be validated.
    :type phone_num: str
    :raises ValueError: If the phone number format is not valid.
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


def register_new_user(phone_num: str) -> bool:
    """
    Registers a new user with a phone number to the service.

    :param phone_num: Phone number to be registered
    :return: True if the registration was successful, False otherwise
    """
    validate_input(phone_num)

    num_registration_url = (
        "http://hackathons.masterschool.com:3030/team/registerNumber"
    )
    payload = {"phoneNumber": phone_num, "teamName": TEAMNAME}
    request_headers = {"Content-Type": "application/json"}
    res = requests.post(
        url=num_registration_url, headers=request_headers, json=payload
    )
    print(f"request status code: {res.status_code}")
    if res.status_code == 200:
        print(
            f"Successfully register the number {phone_num} to team {TEAMNAME}"
        )
        return True
    else:
        print(f"Can not register the number {phone_num} to team {TEAMNAME}")
        return False


def unregister_user(phone_num: str) -> bool:  # currently not in use
    """
    Unregisters a phone number from the service.

    :param phone_num: Phone number to be unregistered
    :return: True if the unregistration was successful, False otherwise
    """
    validate_input(phone_num)

    # Sending unregister request
    num_unregistration_url = (
        "http://hackathons.masterschool.com:3030/team/unregisterNumber"
    )
    payload = {"phoneNumber": phone_num, "teamName": TEAMNAME}
    request_headers = {"Content-Type": "application/json"}
    res = requests.post(
        url=num_unregistration_url, headers=request_headers, json=payload
    )
    print(f"request status code: {res.status_code}")
    if res.status_code == 200:
        print(
            f"Successfully unregister the number {phone_num} from team {TEAMNAME}"
        )
        return True
    else:
        print(
            f"Can not unregister the number {phone_num} from team {TEAMNAME}"
        )
        return False
