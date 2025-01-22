import asyncio
from datetime import datetime, timedelta

import schedule

from holiday_service import HolidayService
from sms_sender import sending_msg_user

REMINDER_TAG = "reminder"

run = True
reminder_time = "08:00"


def _remind_if_holiday_job(phone_num):
    # get day before next holiday
    next_holiday = HolidayService().get_next_holiday()
    holiday_name = next_holiday["name"]
    next_holiday_date_obj = get_date_obj(next_holiday)
    day_before_next_holiday = next_holiday_date_obj - timedelta(days=1)

    # if next day is a holiday
    if day_before_next_holiday.date() == datetime.now().date():
        # send a reminder message
        msg = f"Hey don't forget, tomorrow is {holiday_name}!"
        sending_msg_user(msg, phone_num)


def get_date_obj(holiday_obj):
    next_holiday_date_str = holiday_obj["date"]
    next_holiday_date_obj = datetime.strptime(
        next_holiday_date_str, "%Y-%m-%d"
    )

    return next_holiday_date_obj


async def start_scheduler():
    """
    Initiate the scheduler and run tasks
    """
    schedule.every().day.at(reminder_time).do(_remind_if_holiday_job, "1234").tag(
        REMINDER_TAG, 1234
    )
    while run:
        schedule.run_pending()
        await asyncio.sleep(1)


def set_reminder_time(phone_num, new_reminder_time):
    """
    Sets a new reminder time removes any previous holiday reminder jobs
    from scheduler and sets a new holiday reminder job with a new reminder time.
    """
    schedule.clear(phone_num)
    # schedule.every().day.at(new_reminder_time).do(_remind_if_holiday_job, phone_num).tag(REMINDER_TAG, phone_num)
    schedule.every(new_reminder_time).seconds.do(
        _remind_if_holiday_job, phone_num
    ).tag(REMINDER_TAG, phone_num)


def stop_scheduler():
    """
    Stops scheduling and delete all scheduled jobs.
    """
    global run
    run = False
    schedule.clear()
