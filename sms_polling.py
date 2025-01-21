import requests
import time
from json_storage import JSONStorage
from dotenv import load_dotenv
import os
import json


load_dotenv()
TEAM_NAME = os.getenv("TEAMNAME")
URL = "http://hackathons.masterschool.com:3030/team/getMessages/"
RUNNING = True
INTERVAL = 5  # seconds


def poll_sms_messages(storage) -> None:
    # while RUNNING:
    # response = requests.get(URL + TEAM_NAME)

    # if response.status_code == 200:
    #     raise Exception("API call failed")

    # data = response.json()
    response = {
        "12345": [
            {
                "text": "SUBSCRIBE TeamAC",
                "receivedAt": "2024-08-22T12:08:02.305+0000",
            }
        ],
        "1232534": [
            {
                "text": "SUBSCRIBE TeadsfsfmAC",
                "receivedAt": "2024-08-22T12:08:02.305+0000",
            },
        ],
    }
    response_str = json.dumps(response)
    storage_data = storage.all()

    # print(data_str)
    # print(storage_data)

    if response_str != storage_data:
        storage_dict = json.loads(storage_data)
        for phone_num_data in response:
            response_num_found = storage_dict.get(phone_num_data, None)
            if response_num_found is not None:
                for storage_message in storage_dict[response_num_found]:
                    response_messsage = response[phone_num_data]
                    

        # storage._save(data)

    time.sleep(INTERVAL)


storage = JSONStorage("db.json")
poll_sms_messages(storage)
