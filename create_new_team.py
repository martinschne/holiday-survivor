import requests


def new_team():
    URL = "http://hackathons.masterschool.com:3030/team/addNewTeam"
    REQ_BODY_JSON = {
        "teamName": "HolidaySurvivors"
    }

    #x = requests.post()
