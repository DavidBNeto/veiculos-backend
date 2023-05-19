from datetime import datetime


# This function returns the current date in the format 'YYYY-MM-DD--HH:MM:SS'
def current_date():
    return datetime.now().strftime("%Y-%m-%d--%H:%M:%S")


# This function tells if a date in string came after another date in string.
# The dates must be in the format 'YYYY-MM-DD--HH:MM:SS'
def is_date_after(date_1: str, date_2: str):
    return datetime.strptime(date_1, "%Y-%m-%d--%H:%M:%S") > datetime.strptime(date_2, "%Y-%m-%d--%H:%M:%S")
