import json
import os

import requests
from dotenv import load_dotenv

from json_storage import JSONStorage
from message_processing import process_message

load_dotenv()

# global constants
TEAM_NAME = os.getenv("TEAMNAME")
URL = "http://hackathons.masterschool.com:3030/team/getMessages/"
RUNNING = True
INTERVAL = 5  # seconds


def poll_sms_messages(storage) -> None:
    # while RUNNING:
    response = requests.get(URL + TEAM_NAME)

    if response.status_code != 200:
        raise requests.exceptions.HTTPError(
            f"Polling request to getMessages API endpoint failed with status code {response.status_code}")
    else:
        response_obj = response.json()
    storage_obj = storage.all()

    response_str = json.dumps(response_obj)
    storage_str = json.dumps(storage_obj)

    # if the response is not equal to storage
    if response_str != storage_str:
        # get over the all phone numbers in response object
        for phone_num in response_obj:
            # if phone number key was found in storage object
            if phone_num in storage_obj:
                # get over all messages under the phone number in response object
                for message in response_obj[phone_num]:
                    # and process just those that are not saved in storage obj
                    if message not in storage_obj[phone_num]:
                        print(f"{phone_num} sent: {message} - MESSAGE NOT SAVED, PROCESSING.")
                        """ NOTE here goes process_message function: """
                        process_message(phone_num, message)
                    else:
                        print(f"{phone_num} sent: {message} - MESSAGE SAVED, SKIPPING.")
            else:  # phone number was not found in storage object
                for message in response_obj[phone_num]:
                    # process all messages for the new number
                    print(f"{phone_num} is new and sent: {message}. - MESSAGE NOT SAVED, PROCESSING.")
                    """ NOTE here goes process_message function: """
                    process_message(phone_num, message)

        storage._save(response_obj)

    # time.sleep(INTERVAL)


storage = JSONStorage("processed_messages.json")
poll_sms_messages(storage)
