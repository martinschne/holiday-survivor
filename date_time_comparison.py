from datetime import datetime

"""
old_time = "2025-01-21T08:39:31.294+0000"
new_time = "2025-01-22T08:56:37.175+0000"
strip_old_time = datetime.strptime("2025-01-22T08:56:37.175+0000","%Y-%m-%dT%H:%M:%S.%f%z" )
strip_new_time = datetime.strptime("2025-01-21T08:39:31.294+0000","%Y-%m-%dT%H:%M:%S.%f%z" )
if strip_new_time > strip_old_time:
    print("the new time is newer than the old time")
else:
    print("the old time is older than the new time")
"""
def get_latest_date(time_1, time_2):
    """
    time_1 und time_2 should have the DateTime Format ISO 8601:
        2025-01-22T08:56:37.175+0000
    :param time_1:
    :param time_2:
    :return:
    """
    strip_time_1 = datetime.strptime(time_1, "%Y-%m-%dT%H:%M:%S.%f%z")
    strip_time_2 = datetime.strptime(time_2, "%Y-%m-%dT%H:%M:%S.%f%z")
    if strip_time_1 > strip_time_2:
        return time_1, strip_time_1
    elif strip_time_1 < strip_time_2:
        return time_2, strip_time_2
    else:
        return time_1, strip_time_1