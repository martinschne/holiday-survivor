import requests


def new_team():
    user_input = str(input("Enter a team name:"))
    URL = "http://hackathons.masterschool.com:3030/team/addNewTeam"
    REQ_BODY = {
        "teamName": user_input
    }
    HEADERS = {
        "Content-Type": "application/json"
    }
    res = requests.post(url=URL, headers=HEADERS, json=REQ_BODY)
    print(f"request status code: {res.status_code}")
    if res.status_code == 200:
        print(f"Successfully create a new team named {user_input}")
        return True
    else:
        print(f"Can not create a new team named {user_input}")
        return False

new_team()
