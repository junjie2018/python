from __future__ import print_function
from collections import namedtuple

Disk = namedtuple('Disk', 'major_number minor_number device_name'
                          'read_count read_merged_count read_sections'
                          'time_spend_reading write_count write_merged_count'
                          'write_sections time_spent_write io_requests'
                          'time_spent_doing_io weighted_time_spent_doing_io')


def get_disk_info(device):
    """
    从/proc/diskstats中读取磁盘的IO信息
    cat /proc/diskstates
        254 ...
    """
    with open("/proc/diskstats") as f:
        for line in f:
            if line.split()[2] == device:
                return Disk(*(line.split()))


def main():
    disk_info = get_disk_info('sda')
    print(disk_info)

    print("磁盘写次数".format(disk_info.write_count))
    print("磁盘写字节数".format(long(disk_info.write_sections) * 512))
    print("磁盘写延时".format(disk_info.time_spent_write))


if __name__ == '__main__':
    main()
