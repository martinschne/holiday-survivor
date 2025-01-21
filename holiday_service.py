import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("HOLIDAY_API_KEY")


class HolidayService:
    def __init__(self):
        self.URL = "https://holidayapi.com/v1/holidays"
        self.key = API_KEY
        self.country = "DE"
        self.day = datetime.now().day
        self.month = datetime.now().month
        self.year = 2024
        self.parameters = {
            "country": self.country,
            "year": self.year,
            "key": self.key,
        }

    def get_next_holiday(self):
        """
        Get the name of the next holiday in the specified country.

        :return: The name of the next holiday, or None if there is no next holiday.
        :rtype: str
        """
        response = requests.get(url=self.URL, params=self.parameters)
        if response.status_code != 200:
            raise Exception("API call failed")

        data = response.json()

        for i, holiday in enumerate(data["holidays"]):
            date_str = holiday["date"]
            date = datetime.strptime(date_str, "%Y-%m-%d")
            today = datetime(year=self.year, month=self.month, day=self.day)
            fake_today = today.replace(year=self.year)
            if date > fake_today:
                return holiday

        return data["holidays"][0]

    def get_all_holidays(self):
        """
        Get a list of all holidays for the specified country in the specified year.

        :return: A list of dictionaries with information about each holiday.
        :rtype: list
        """
        response = requests.get(url=self.URL, params=self.parameters)
        if response.status_code != 200:
            raise Exception("API call failed")

        data = response.json()

        for i, holiday in enumerate(data["holidays"]):
            date_str = holiday["date"]
            date = datetime.strptime(date_str, "%Y-%m-%d")
            today = datetime(year=self.year, month=self.month, day=self.day)
            fake_today = today.replace(year=2024)
            if date > fake_today:
                return data["holidays"][i:]

        return []
