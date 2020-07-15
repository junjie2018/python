import _thread
import queue
import sys
import threading
import time

"""
    _thread模块中，主线程退出，子线程将会自动退出。在threading模块中，如果任何一个派生线程仍在运行中
    程序不会退出，除非那些线程被设定为守护线程。Python的初始线程不是守护线程。
    
    严格来说，Python目前使用的是本节最开始介绍的全局解释器锁机制，它可以确保任意给定时间点最多只有一
    个线程在Python解释器中运行代码。此外，为确保每个线程都得到运行的机会，解释器在线程间每隔固定的间
    隔期，以及长时运行操作系统开始时（比如接收文件输入/输出请求时），自动切换焦点（好吧，这段是在是太
    深入了，我不太理解）
"""

numconsumers = 2
numproducers = 4
nummessages = 4

safe_print = _thread.allocate_lock()
data_queue = queue.Queue()


def producer(idnum):
    for msgnum in range(nummessages):
        time.sleep(idnum)
        data_queue.put('[producer id=%d, count=%d]' % (idnum, msgnum))


def consumer(idnum):
    while True:
        time.sleep(0.1)
        try:
            data = data_queue.get(block=False)
        except queue.Empty:
            pass
        else:
            with safe_print:
                print('consumer', idnum, 'got =>', data)


def queuetest_main():
    for i in range(numconsumers):
        _thread.start_new_thread(consumer, (i,))
    for i in range(numproducers):
        _thread.start_new_thread(producer, (i,))
    time.sleep((numproducers - 1) * nummessages + 1)
    print('Main thread exit.')


def queuetest2_main():
    for i in range(numproducers):
        thread = threading.Thread(target=producer, args=(i, data_queue))
        thread.daemon = True
        thread.start()

    waitfor = []
    for i in range(numconsumers):
        thread = threading.Thread(target=consumer, args=(i, data_queue))
        thread.start()
        waitfor.append(thread)

    for thread in waitfor: thread.join()
    print('Main thread exit.')


def timer_test():
    t = threading.Timer(5.5, lambda: print('Spam!'))

    t.start()


def timer_test2():
    from tkinter import Tk
    from tkinter.messagebox import showinfo
    win = Tk()
    win.after(5500, lambda: showinfo('Popup', 'Spam!'))


if __name__ == '__main__':
    eval(sys.argv[1])()
