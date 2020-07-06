import psutil
import datetime

print(psutil.users())
print(datetime.datetime.formatstamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))
