"""
    os.open(path,flags, mode)               ：打开文件并返回描述符
    os.read(descriptor, N)                  ：最多读取N个字节，并返回一个字节字符串
    os.write(descriptor, string)            ：把字节字符串string中的字节写入文件
    os.lseek(descriptor, position, how)     ：在文件中移至position

    某系系统上，os.open的标识符可以让我们在打开文件时指定更高级的参数，比如唯一访问权（O_EXCL）
    和非阻塞模式（O_NONBLOCK）。有些标识符是不能跨平台移植的（这也是大多数时候使用内建文件的另
    一个原因。

    带有O_EXCL标识符的os.open标识符的os.open现在是Python中在并发或其他进程同步情况下锁定文件
    的最便捷的方法。

    对于相关工具，还可以参考Python标准库中的shutil模块，它拥有更高级工具，可用于复制和删除文
    件等操作。在学习本章后续部分中的目录工具之后，我们还会在第6章中编写自己的目录比较，复制和
    搜索工具。

"""
import os
import sys

for stream in (sys.stdin, sys.stdout, sys.stderr):
    print(stream.fileno())

sys.stdout.write('Hello stdio world\n')
os.write(1, b'Hello descriptor world\n')

file = open('data.txt', 'w')
file.write('Hello stdio file\n')
file.flush()
fd = file.fileno()
print(fd)

os.write(fd, b'Hello descriptor file\n')
file.close()

fd = os.open('data.txt', (os.O_RDWR | os.O_BINARY))
print(os.read(fd, 20))
os.lseek(fd, 0, 0)
print(os.read(fd, 100))
os.lseek(fd, 0, 0)
os.write(fd, b'HELLO')

file = open('data.txt', 'rb+')
print(file.read(20))
file.seek(0)
print(file.read(200))
file.seek(0)
file.write(b'JELLO')
file.seek(0)
print(file.read())
file.flush()
file.close()

# os.rename('data2.txt', 'data3.txt')
# os.remove('data3.txt')

fd = os.open('data.txt', (os.O_RDWR | os.O_BINARY))
fd2 = os.fdopen(fd, 'r')
print(fd2.read())

fd = os.open('data.txt', (os.O_RDWR | os.O_BINARY))
fd2 = os.fdopen(fd, 'rb')
print(fd2.read())

fd3 = open(fd, 'r', encoding='latin1', closefd=False)
print(fd3.read())
fd3 = open(fd, 'r', encoding='latin1', closefd=False)
fd3.seek(0)
print(fd3.read())
