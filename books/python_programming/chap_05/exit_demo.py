import _thread
import os
import sys
import threading
import time
from subprocess import Popen, PIPE, call

"""
    sys和os退出调用接收进程退出状态代码作为参数（在sys模块调用中为可选，但在os模块中为必需）。退出
    后，这个状态代码可以在shell中查询，也可以以子进程运行该脚本的程序中查询。在Linux下，我们访问
    status这个shell变量以获得上一个程序的退出状态（echo $? echo $status）。
"""


def later():
    print('Byte sys world')
    sys.exit(42)


def later_main():
    try:
        later()
    except SystemExit:
        print('Ingore...')
    finally:
        print('cleanup')


def outahere():
    """
        对于os._exit，调用进程理解退出，而不是抛出异常或忽略异常。事实上，进程退出时也不输出流缓冲和
        运行清理处理器（由atexit标准库模块定义），所以这种做法一般应当只在分支出的子进程上进行，而最
        好不用于这个程序退出行为。
    """
    print('Bye os world')
    os._exit(99)


def outahere_test():
    outahere()


def exit_status():
    pipe = os.popen('python test.py')
    print(pipe.read())
    stat = pipe.close()

    pipe = os.popen('python test.py')
    stat = pipe.close()


def exit_stream():
    pipe = os.popen('python test.py')
    print(pipe.read())  # ''
    pipe = os.popen('python -u test.py')  # 强制无缓冲流
    print(pipe.read())  # 'Bye os world\n'

    """
        让人觉得困惑的是：你可以在os.popne和subprocess.Popen中传入模式和缓冲参数以指定行缓冲，
        不过在这个实例中却没有用，因为传入这些工具的参数数据调用进程的管道的输入端，而不属于派
        生程序的输出流：（也就是说我们的管道会一行一刷新，但是程序还是不会刷新到管道上么？）
    """
    pipe = os.popen('python testexit_os.py', 'r', 1)
    print(pipe.read())  # ''

    pipe = Popen('python testexit_os.py', bufsize=1, stdout=PIPE)
    print(pipe.stdout.read())  # b''

    pipe = Popen('python testexit_sys.py', stdout=PIPE)
    print(pipe.stdout.read())
    print(pipe.wait())  # 一种读取返回值的方式
    print(call('python testexit_sys.py'))  # 一种读取返回值的方式

    pipe = Popen('python testexit_sys.py', stdout=PIPE)
    print(pipe.communicate())
    print(pipe.returncode)  # 一种读取返回值的方式

    """
        subprocess模块在Unix平台上的使用方法和Cygwin相同。不过和os.popen不同的是，它的退出状态
        没有被编码，因此与windows下的结果可以匹配。
    """
    pipe = Popen('python testexit_sys.py', stdout=PIPE, shell=True)
    print(pipe.stdout.read())
    print(pipe.wait())

    print(call('pthon testexit_sys.py', shell=True))


exit_stat = 0


def child():
    global exit_stat
    exit_stat += 1
    print('Hello from child', os.getpid(), exit_stat)
    os._exit(exit_stat)
    print('never reached')


def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            pid, status = os.wait()  # 这样就可以拿到子进程的返回值了
            print('Parent got', pid, status, (status >> 8))
            if input() == 'q': break


def test_exit_fork_main():
    parent()


def child2():
    global exit_stat
    exit_stat += 1
    threadid = _thread.get_ident()
    print('Hello from child', threadid, exit_stat)
    _thread.exit()
    print('never reached')


def parent2():
    while True:
        _thread.start_new_thread(child, ())
        if input() == 'q': break


def test_exit_thread():
    parent2()


def action():
    sys.exit()


def threading_exit_test():
    threading.Thread(target=action).start()
    time.sleep(2)
    print('Main exit')


if __name__ == '__main__':
    eval(sys.argv[1])()
