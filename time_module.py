from datetime import datetime


def get_time():
    now = datetime.now()

    current_time = now.strftime("%H hours %M minutes")
    return current_time


def get_hours():
    now = datetime.now()
    return(now.strftime("%H"))
