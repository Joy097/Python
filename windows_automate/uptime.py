import psutil
import time
import math

def convert_seconds(seconds):
    minutes, sec = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    return math.ceil(days),math.ceil(hours), math.ceil(minutes), math.ceil(sec)



seconds = time.time() - psutil.boot_time()
days, hours, minutes, seconds = convert_seconds(seconds)
print("\r Uptime: {} days, {} hours, {} minutes, {} seconds".format(days, hours, minutes, seconds),end="")


