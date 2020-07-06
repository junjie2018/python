import psutil

# cpu
print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))

print(psutil.cpu_percent())
print(psutil.cpu_percent(percpu=True))
print(psutil.cpu_percent(percpu=True, interval=2))

print(psutil.cpu_times())
print(psutil.cpu_times_percent())

print(psutil.cpu_stats())
