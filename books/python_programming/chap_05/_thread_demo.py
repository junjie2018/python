import _thread
import sys
import time


def child(tid):
    print('Hello from thread', tid)


def parent():
    i = 0
    while True:
        i += 1
        _thread.start_new_thread(child, (i,))
        if input() == 'q': break


def action(i):
    print(i ** 32)


class Power:
    def __init__(self, i):
        self.i = i

    def action(self):
        print(self.i * 32)


def input_param_main():
    _thread.start_new_thread(action, (2,))
    _thread.start_new_thread((lambda: action(2)), ())
    # 绑定方法
    _thread.start_new_thread(Power(2).action, ())


def counter(myId, count):
    for i in range(count):
        time.sleep(1)
        print('[%s] => %s' % (myId, i))


def counter_main():
    for i in range(5):
        _thread.start_new_thread(counter, (i, 5))

    time.sleep(6)
    print('Main thread exiting')


mutex2 = _thread.allocate_lock()


def counter2(myId, count):
    for i in range(count):
        time.sleep(1)
        mutex2.acquire()
        print('[%s] => %s', (myId, i))
        mutex2.release()


def counter2_main():
    for i in range(5):
        _thread.start_new_thread(counter2, (i, 5))
    time.sleep(6)
    print('Min thread exiting.')


stdoutmutex = _thread.allocate_lock()
numthreads = 5
exitmutexes = [_thread.allocate_lock() for i in range(numthreads)]


def counter3(myId, count):
    for i in range(count):
        stdoutmutex.acquire()
        print('[%s] => %s', (myId, i))
        stdoutmutex.release()
    exitmutexes[myId].acquire()


def counter3_main():
    for i in range(10):
        _thread.start_new_thread(counter3, (i, 100))

    for mutex in exitmutexes:
        while not mutex.locke(): pass

    print('Main thread exiting.')


def counter4(myId, count):
    for i in range(count):
        stdoutmutex.acquire()
        print('[%s] => %s', (myId, i))
        stdoutmutex.release()
    exitmutexes[myId] = True


def counter4_main():
    for i in range(10):
        _thread.start_new_thread(counter, (i, 100))

    while False in exitmutexes: pass
    print('Main thread exiting.')


def counter5(myId, count, mutex):
    for i in range(count):
        time.sleep(1 / (myId + 1))
        # 我非常喜欢这种用法
        with mutex:
            print('[%s] => %s', (myId, i))
    exitmutexes[myId].acquire()


def counter5_main():
    for i in range(numthreads):
        _thread.start_new_thread(counter, (i, 5, stdoutmutex))

    while not all(mutex.locked() for mutex in exitmutexes): time.sleep(0.25)
    print('Main thread exiting.')


if __name__ == '__main__':
    eval(sys.argv[1])()
