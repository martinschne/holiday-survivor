import re
import time
from datetime import datetime

from holiday_service import HolidayService
from sms_sender import sending_msg_user

REMINDER_PATTERN = r"^REMINDER\s*((?:[01]?\d|2[0-3]):[0-5]\d)"
NEXT_HOLIDAY_PATTERN = r"^NEXT\s*HOLIDAY$"
INSTRUCTIONS_PATTERN = r"^INSTRUCTIONS"


def process_message(phone_num, message):
    """
    Processes an incoming message and performs actions based on the content of the message.

    This function normalizes the message text, matching it against predefined patterns
    to identify specific commands. Depending on the match, it performs one of the following:
    - Sets a reminder time if the message matches the REMINDER_PATTERN.
    - Sends information about the next holiday if the message matches the NEXT_HOLIDAY_PATTERN.
    - Sends instructions if the message matches the INSTRUCTIONS_PATTERN.
    - Sends an error message if no known pattern is matched.

    Parameters:
    phone_num (str): The phone number of the user who sent the message.
    message (Message): The message object containing the text to be processed.
    """
    print(message)
    normalized_message_text = message["text"].strip().upper()

    if re.match(REMINDER_PATTERN, normalized_message_text):
        reminder_time = re.match(
            REMINDER_PATTERN, normalized_message_text
        ).group(1)
        _set_reminder_time(phone_num, reminder_time)
    elif re.match(NEXT_HOLIDAY_PATTERN, normalized_message_text):
        _send_next_holiday(phone_num)
    elif re.match(INSTRUCTIONS_PATTERN, normalized_message_text):
        _send_instructions(phone_num)
    else:  # no known pattern was matched
        _send_error_message(phone_num)


def _set_reminder_time(phone_num, reminder_time):
    msg = (
            f"🎉 Reminder successfully set at {reminder_time}.\n"
            + f"You will get a notification one day before each holiday at {reminder_time}."
    )

    sending_msg_user(msg, phone_num)

    # set scheduler
    # scheduler.set_reminder_time(phone_num, reminder_time)

    # fake message for presentation
    time.sleep(10)
    fake_msg = "Hey don´t forget, tomorrow is Holiday Survivors Day!"
    sending_msg_user(fake_msg, phone_num)


def _send_next_holiday(phone_num):
    holiday_service = HolidayService()
    holiday_obj = holiday_service.get_next_holiday()
    date = datetime.strptime(holiday_obj["date"], "%Y-%m-%d")
    msg = f"{holiday_obj['name']} at {date.day}-{date.month}-{date.year + 1}"
    sending_msg_user(msg, phone_num)


def _send_instructions(phone_num):
    msg = """Usage Instructions:
instructions: to receive usage instructions
reminder hh:mm: (for example reminder 08:30) to set a time for holiday reminder
next holiday: to receive next holiday"""
    sending_msg_user(msg, phone_num)


def _send_error_message(phone_num):
    msg = "Wrong Command, please respond with text 'instructions' to receive usage instructions."
    sending_msg_user(msg, phone_num)
