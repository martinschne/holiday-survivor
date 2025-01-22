import re
from datetime import datetime
from sms_sender import sending_msg_user
from holiday_service import HolidayService

REMINDER_PATTERN = r"^REMINDER\s*((?:[01]?\d|2[0-3]):[0-5]\d)"
NEXT_HOLIDAY_PATTERN = r"^NEXT\s*HOLIDAY$"
# ALL_HOLIDAYS_PATTERN = r"^ALL\s*HOLIDAYS$"
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
        reminder_time = re.match(REMINDER_PATTERN, normalized_message_text).group(1)
        _set_reminder_time(phone_num, reminder_time)
    elif re.match(NEXT_HOLIDAY_PATTERN, normalized_message_text):
        _send_next_holiday(phone_num)
    elif re.match(INSTRUCTIONS_PATTERN, normalized_message_text):
        _send_instructions(phone_num)
    else:  # no known pattern was matched
        _send_error_message(phone_num)


def _set_reminder_time(phone_num, reminder_time):
    pass


def _send_next_holiday(phone_num):
    holiday_service = HolidayService()
    holiday_obj = holiday_service.get_next_holiday()
    date = datetime.strptime(holiday_obj['date'], "%Y-%m-%d")
    msg = f"{holiday_obj['name']} at {date.day}-{date.month}-{date.year + 1}"
    sending_msg_user(msg, phone_num)


def _send_instructions(phone_num):
    msg = """
    'instructions': to get instructions
    'reminder hh:mm': to set a time reminder for the holiday
    'next holiday': to see the next holiday
    """
    sending_msg_user(msg, phone_num)


def _send_error_message(phone_num):
    msg = "Wrong Command, please send an sms with 'instructions' text to get possible commands."
    sending_msg_user(msg, phone_num)
