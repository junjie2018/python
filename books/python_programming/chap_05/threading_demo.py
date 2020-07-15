import _thread
import sys
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, myId, count, mutex):
        self.myId = myId
        self.count = count
        self.mutex = mutex

    def run(self):
        for i in range(self.count):
            with self.mutex:
                print('[%s] => %s' % (self.myId, i))


def my_thread_main():
    stdout_mutex = threading.Lock()
    threads = []
    for i in range(10):
        thread = MyThread(i, 100, stdout_mutex)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()  # 书中写的是start()，但是很明显是错误的
    print('Main thread exiting.')


def action(i):
    print(i ** 32)


class MyThread2(threading.Thread):
    def __init__(self, i):
        self.i = i
        threading.Thread.__init__(self)

    def run(self):
        print(self.i * 32)


def threading_main():
    # case 1:
    MyThread2(2).start()

    # case 2:
    thread = threading.Thread(target=(lambda: action(2)))
    thread.start()

    # case 3:
    threading.Thread(target=action, args=(2,)).start()

    # case 4:
    _thread.start_new_thread(action, (2,))


class Power:
    def __init__(self, i):
        self.i = i

    def action(self):
        print(self.i ** 32)


def action2(i):
    def power():
        print(i ** 32)

    return power


def power_main():
    threading.Thread(target=Power(2).action()).start()
    threading.Thread(target=action2(2)).start()

    _thread.start_new_thread(Power(2).action, ())
    _thread.start_new_thread(action2(2), ())


count = 0


def adder():
    global count
    count = count + 1
    time.sleep(1)
    count = count + 1


def thread_add_random():
    """
        问题我知道，尴尬的是我机器上做不出这个效果
    """
    threads = []
    for i in range(100):
        thread = threading.Thread(target=adder, args=())
        thread.start()
        threads.append(thread)
    for thread in threads: thread.join()
    print(count)
    return count


def adder2(addlock):
    global count
    with addlock:
        count = count + 1
    time.sleep(0.5)
    with addlock:
        count = count + 1


def thread_add_synch():
    addlock = threading.Lock()
    threads = []
    for i in range(100):
        thread = threading.Thread(target=adder2, args=(addlock,))
        thread.start()
        threads.append(thread)

    for thread in threads: thread.join()


if __name__ == '__main__':
    # eval(sys.argv[1])()
    for i in range(1000):
        res = thread_add_random()

        if res != 200:
            break

        count = 0
