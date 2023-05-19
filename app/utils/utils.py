from datetime import datetime


# This function returns the current date in the format 'YYYY-MM-DD--HH:MM:SS'
def current_date():
    return datetime.now().strftime("%Y-%m-%d--%H:%M:%S")
