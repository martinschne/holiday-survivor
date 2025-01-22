from datetime import datetime

import requests
from config import HOLIDAY_API_KEY as API_KEY

URL = "https://holidayapi.com/v1/holidays"
COUNTRY_CODE = "DE"
TODAY = datetime.now()
FAKE_YEAR = 2024  # set the current year to 2024 because the API doesn't have data for 2025


class HolidayService:
    def __init__(self):
        """
        Initialize a new HolidayService object.

        The object will be initialized with the current month and day, and the year 2024.
        The API key will be read from the environment variable `HOLIDAY_API_KEY`.
        The country code will be `DE` for Germany.

        :param: None
        :return: None
        """
        self.URL = URL
        self.key = API_KEY
        self.country = COUNTRY_CODE
        self.day = TODAY.day
        self.month = TODAY.month
        self.year = FAKE_YEAR
        self.parameters = {
            "country": self.country,
            "year": self.year,
            "key": self.key,
        }

    def get_next_holiday(self) -> dict:
        """
        Get the name of the next holiday in the specified country.

        This method will find the first holiday in the list of holidays which is
        after the current date. If no such holiday is found, it will return the
        first holiday in the list. This means that if the current date is after
        the last holiday of the year, it will return the first holiday of the
        next year.

        This method will return `None` if there is no next holiday in the current year.

        :return: The holiday object, or None if there is no next holiday.
        :rtype: dict
        """
        response = requests.get(url=self.URL, params=self.parameters)
        if response.status_code != 200:
            raise Exception("API call failed")

        data = response.json()

        # Find the first holiday which is after the current date.
        for i, holiday in enumerate(data["holidays"]):
            date_str = holiday["date"]
            date = datetime.strptime(date_str, "%Y-%m-%d")
            today = datetime(year=self.year, month=self.month, day=self.day)
            fake_today = today.replace(year=self.year)
            if date > fake_today:
                return holiday

        # If no holiday is found, return the first holiday in the list.
        # This is the case if the current date is after the last holiday of the year.
        # This is a hack to fake the next holiday without having access to the API
        return data["holidays"][0]

    # This method is not used in the current app state
    def get_all_holidays(self) -> list:
        """
        Get a list of all holidays for the specified country in the specified year.

        This method will return all holidays in the list of holidays which are
        after the current date. If no such holidays are found, it will return an
        empty list. This means that if the current date is after the last holiday
        of the year, it will return an empty list.

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
                # Return all holidays which are after the current date
                return data["holidays"][i:]

        # Return an empty list if no holidays are after the current date
        # This is the case if the current date is after the last holiday of the year
        # and there are no holidays for the current year
        return []
