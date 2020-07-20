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


def spawn(prog, *args):
    stdinFd = sys.stdin.fileno()
    stdoutFd = sys.stdout.fileno()

    parentStdin, childStdout = os.pipe()
    childStdin, parentStdout = os.pipe()

    pid = os.fork()
    if pid:
        os.close(childStdout)
        os.close(childStdin)
        os.dup2(parentStdin, stdinFd)
        os.dup2(parentStdout, stdoutFd)
    else:
        os.close(parentStdin)
        os.close(parentStdout)
        os.dup2(childStdin, stdinFd)
        os.dup2(childStdout, stdoutFd)
        args = (prog,) + args
        os.execvp(prog, args)
        assert False, 'execvp failed!'


def spawn_main():
    """
        os.dup2(fd1,fd2):把由文件描述符fd1命名的文件的所有相关系统信息复制到有fd2命名的文件中
    :return:
    """

    mypid = os.getpid()
    spawn('python', 'pipes-testchild.py', 'spam')

    print('Hello 1 from parent', mypid)
    sys.stdout.flush()
    reply = input()
    sys.stderr.write('Parent got: "%s"\n' % reply)

    print('Hello 2 from parent', mypid)
    sys.stdout.flush()
    reply = sys.stdin.readline()
    sys.stderr.write('Parent got: "%s"\n' % reply[:-1])


if __name__ == '__main__':
    eval(sys.argv[1])()
