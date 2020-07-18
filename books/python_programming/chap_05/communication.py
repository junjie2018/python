import os
import sys
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
        pipein = os.fdopen(pipein)
        while True:
            line = pipein.readline()[:-1]
            print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()))


if __name__ == '__main__':
    eval(sys.argv[1])()
