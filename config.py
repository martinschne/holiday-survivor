import os

from dotenv import load_dotenv

load_dotenv()
TEAMNAME = os.getenv("TEAMNAME")
MASTERSCHOOL_API_PHONE_NUMBER = os.getenv("MASTERSCHOOL_API_PHONE_NUMBER")
HOLIDAY_API_KEY = os.getenv("HOLIDAY_API_KEY")
