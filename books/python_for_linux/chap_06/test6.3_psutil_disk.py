import psutil


def get_disk_via_mountpint(mountpoint):
    disk = [item for item in psutil.disk_partitions()
            if item.mountpoint == mountpoint]
    return disk[0].device


# disk
print(psutil.disk_partitions)
print(get_disk_via_mountpint('/'))
print(get_disk_via_mountpint('ebs'))

print(psutil.disk_io_counters())
print(psutil.disk_io_counters(predisk=True))
