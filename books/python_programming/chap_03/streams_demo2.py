import os
import sys
from subprocess import Popen, PIPE, call


def hello_out():
    print('Hello shell world')


def hello_in():
    inp = input()
    open('data.txt', 'w').write('Hello ' + inp + '\n')


def test_os_popen():
    pipe = os.popen('python streams_demo2.py hello_out')
    print(pipe.read())
    print(pipe.close())

    pipe = os.popen('python streams_demo2.py hello_in', 'w')
    pipe.write('Gumby\n')
    pipe.close()


def test_subprocess_popen():
    """
        第一种方式中的call是一个方便函数，第二种的communicate只是第三种方式的易用版本（它
        发送数据到stdin，从stdou中读取数据知道文件末，并等待进程结束）
    """
    X = call('python streams_demo2.py hello_out')
    print(X)

    pipe = Popen('python streams_demo2.py hello_out', stdout=PIPE)
    print(pipe.communicate()[0])
    print(pipe.returncode)

    pipe = Popen('python streams_demo2.py hello_out', stdout=PIPE)
    print(pipe.stdout.read())
    print(pipe.wait())

    pipe = Popen('python streams_demo2.py hello_in', stdin=PIPE)
    print(pipe.stdin.write(b'Pokey\n'))
    print(pipe.stdin.close())
    print(pipe.wait())


def test_subprocess_popen2():
    """
        当与程序反复交互时需要谨慎对待：如果读写是交替发生的，缓冲流额能导致死锁，可能需要
        使用类似Pexpect等工作作为变通方案
    """

    pipe = Popen('python streams_demo.py reader', stdin=PIPE, stdout=PIPE)
    pipe.stdin.write(b'Lumberjack\n')
    pipe.stdin.write(b'12\n')
    pipe.stdin.close()
    output = pipe.stdout.read()
    pipe.wait()
    print(output)

    # 这个很高大上
    pipe1 = Popen('python streams_demo.py writer', stdout=PIPE)
    pipe2 = Popen('python streams_demo.py reader', stdin=pipe1.stdout, stdout=PIPE)

    output = pipe2.communicate()[0]
    print(output)
    print(pipe2.returncode)

    # 这个不高大上
    pipe1 = os.popen('python streams_demo.py writer', 'r')
    pipe2 = os.popen('python streams_demo.py reader', 'w')
    pipe2.write(pipe1.read())

    X = pipe2.close()
    print(X)


if __name__ == '__main__':
    choice = sys.argv[1]
    eval(choice)()
