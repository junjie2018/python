import psutil
import datetime

init_process = psutil.Prcess(1)
print(init_process.cmdline())

# 返回当前正在运行的进程
print(psutil.pids()[:5])

print(psutil.pid_exists(1))
print(psutil.pid_exists(12345))
