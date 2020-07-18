import os
import sys
import threading
import time


def child(pipeout):
    zzz = 0
    while True:
        time.sleep(zzz)
        msg = ('Spam %03d' % zzz).encode()
        os.write(pipeout, msg)
        zzz = (zzz + 1) % 5


def parent():
    pipein, pipeout = os.pipe()
    if os.fork() == 0:
        child(pipeout)
    else:
        while True:
            line = os.read(pipein, 32)
            print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()))


def child2(pipeout):
    zzz = 0
    while True:
        time.sleep(zzz)
        msg = ('Spam %03d\n' % zzz).encode()
        os.write(pipeout, msg)
        zzz = (zzz + 1) % 5


def parent2():
    pipein, pipeout = os.pipe()
    if os.fork() == 0:
        os.close(pipein)
        child2(pipeout)
    else:
        os.close(pipeout)
        # os.fdopen() 方法用于通过文件描述符 fd 创建一个文件对象，并返回这个文件对象。(我印象不是很深)
        pipein = os.fdopen(pipein)
        while True:
            line = pipein.readline()[:-1]
            print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()))


def child3(pipeout):
    zzz = 0
    while True:
        time.sleep(zzz)
        msg = ('Spam %03d' % zzz).encode()
        os.write(pipeout, msg)
        zzz = (zzz + 1) % 5


def parent3(pipein):
    while True:
        line = os.read(pipein, 32)
        print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()))


def parent3_main():
    pipein, pipeout = os.pipe()
    threading.Thread(target=child, args=(pipeout,)).start()
    parent3(pipein)


if __name__ == '__main__':
    eval(sys.argv[1])()

