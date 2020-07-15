"""
    分支的想法基于程序复制：当程序调用分支例行程序时，操作系统会创建该程序及其在内存中的进程的副本，
    然后开始与原有程序并行地运行该副本。

    window上无法进行该实验，parent的这种写法和c语言很像，比较容易理解
"""
import os
import time


def child():
    print('Hello from child', os.getpid())
    os._exit(0)


def parent():
    """
        由os模块提供的Python进程分支工具仅仅是系统代码库里标准进程分支调用进行简单封装后的结果，这个代码库
        同时还未C语言所使用。想要启动新的并行进程，调用os.fork的内建函数即可。因为这个函数调用为调用程序创
        建了一个副本，所以它为每份副本返回不同的值：在子进程中返回0，而在父进程中返回新进程的ID。

        在当前的Python中，在Python脚本中调用os.fork实际上是对Python交互解释器进程进行了复制（如果你查看进
        程列表，可以在分支操作后看到两个Python项）。但是因为Python交互解释器记录了正在运行脚本的方方面面，
        所以可以吧分支看成直接复制了你的程序。而如果Python脚本编译成二进制机器码，那就确实是这样执行的。

    """
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            print('Hello from parent', os.getpid(), newpid)
        if input() == 'q': break


def counter(count):
    for i in range(count):
        time.sleep(1)
        print('[%s] => %s' % (os.getpid(), i))


def counter_test():
    """
        所有这些进程的输出结果在同一个屏幕上显示，因为他们都共享标准输出流（系统提示符可能也会在其中显示）。
        从技术层面来说，分支进程得到原来进程的全局内存中内容的副本，包括所打开文件的描述符。因此，文件等全局
        对象在子进程开始时具有同样的值，这里的所有进程才绑定到同一个输出流上。但是需要记住，全局内存是被复制
        了而非共享的。如果某一个子进程改变了某个全局对象，那它只是改变了自己的副本。
    """
    for i in range(5):
        pid = os.fork()
        if pid != 0:
            print('Process %d spawned' % pid)
        else:
            counter(5)
            os._exit(0)
    print('Main process exiting.')


def execlp():
    """
        os.execlp调用可以用一个全新的程序代替（即执行覆盖）当前进程中正运行的程序。由于这个原因，
        os.fork和os.execlp的组合意味着开始一个新的进程，并在其中运行一个新的程序。

        os.execlp的参数是通过指定即将运行的程序命令行参数来启动程序（即Python脚本中的sys.argv）。
        启动成功则开始运行新的程序，而os.execlp调用却不会返回（因为原先的程序已经被替换，没有返回
        的目标对象了）。如果调用返回，则表示发生了错误，因此我们在后面编写了一句assert语句，以便抛
        出异常。

        os.execv(program,commandlinessequence)
            基本的v执行形式，需要传入可执行程序的名称，以及用来运行程序的命令行参数数字字符串组成
            （即你在shell中起始程序通常输入的语句）的列表或元祖

        os.execl(program,cmdarg1,cmdarg2,cmdargN)
            基本的l执行形式，需要传入可执行明旭的名称，以及一个或多给以单个的函数参数形式传入的命
            令行参数，相当于运行os.evecv(program,(cmdarg1,cmdarg2,...))

        os.execlp os.execvp
            在execv和ececl后面加上字幕p表示Python将使用你的系统搜索路径设置（即PATH）来定位可执
            行程序的目录

        os.execle os.execve
            在execv和execl后面加上字母e表示将在最后添加一个参数，这个参数是一个字典，包含将发送
            给程序的shell环境变量

        os.execvpe os.execlpe
            在基本的exce函数后添加字母p和e表示使用搜索路径并接受shell环境变量字典参数
    """
    param = 0
    while True:
        pid = os.fork()
        if pid == 0:
            # 我不是很理解这个参数传递的方式，为什么要传递两个'python'？
            os.execlp('python', 'python', 'child.py', str(param))
            assert False, 'error starting program'
        else:
            print('Child is', pid)
            if input == 'q': break


if __name__ == '__main__':
    parent()
