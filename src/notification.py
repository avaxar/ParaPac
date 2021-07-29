import time
from src import common

# Notification : (text, duration, time_started)
notifications = []


def new_notif(text, duration):
    try:
        # if not notifications[-1][0] == text:
        notifications.append((common.font.render(text, False, (255, 255, 255)), duration, time.perf_counter()))
    except IndexError:
        pass
