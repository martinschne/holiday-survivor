import time
import asyncio
import schedule

REMINDER_TAG = "reminder"

run = True
reminder_time = "08:00"


def _remind_if_holiday_job(phone_num):
    # get all holidays
    # if next day is a holiday
    # send a reminder message
    print(f"{phone_num} reminder")


async def start_scheduler():
    """
    Initiate the scheduler and run tasks
    """
    schedule.every().day.at().do(_remind_if_holiday_job, "1234").tag(REMINDER_TAG, 1234)
    while run:
        schedule.run_pending()
        asyncio.sleep(1)


def set_reminder_time(phone_num, new_reminder_time):
    """
    Sets a new reminder time removes any previous holiday reminder jobs
    from scheduler and sets a new holiday reminder job with a new reminder time.
    """
    schedule.clear(phone_num)
    # schedule.every().day.at(new_reminder_time).do(_remind_if_holiday_job, phone_num).tag(REMINDER_TAG, phone_num)
    schedule.every(new_reminder_time).seconds.do(_remind_if_holiday_job, phone_num).tag(REMINDER_TAG, phone_num)


def stop_scheduler():
    """
    Stops scheduling and delete all scheduled jobs.
    """
    global run
    run = False
    schedule.clear()


async def main():
    asyncio.create_task(start_scheduler())
    set_reminder_time("1234", 3)
    set_reminder_time("12345", 3)

    # Keep the program running indefinitely
    await asyncio.get_event_loop().run_forever()

asyncio.run(main())