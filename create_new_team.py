import requests


def new_team():
    user_input = str(input("Enter a team name:"))
    team_creation_url = "http://hackathons.masterschool.com:3030/team/addNewTeam"
    payload = {
        "teamName": user_input
    }
    request_headers = {
        "Content-Type": "application/json"
    }
    res = requests.post(url=team_creation_url, headers=request_headers, json=payload)
    print(f"request status code: {res.status_code}")
    if res.status_code == 200:
        print(f"Successfully create a new team named {user_input}")
        return True
    else:
        print(f"Can not create a new team named {user_input}")
        return False


new_team()
