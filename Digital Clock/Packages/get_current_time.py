from datetime import datetime

def get_current_time():
    # get and return current time, hour, minute and second
    ctime = datetime.now()
    hour = str(ctime.hour)
    minute = str(ctime.minute)
    second = str(ctime.second)
    if(len(hour) < 2):
        hour = f"0{hour}"
    if(len(minute) < 2):
        minute = f"0{minute}"
    if(len(second) < 2):
        second = f"0{second}"
    return ctime, hour, minute, second