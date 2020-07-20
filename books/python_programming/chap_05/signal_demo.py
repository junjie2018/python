import sys, signal, time


def now():
    return time.ctime(time.time())


def on_signal(signum, stackframe):
    print('Got signal', signum, 'at', now())


def on_signal_main():
    """
        signal.signal:
            接收信号编号和函数对象，布置该函数为信号编号抛出时的处理器。Python在信号出现时自动
            恢复大多数信号处理器，所以没有必要再信号处理器内部再次调用这个函数来重新登记处理器。
            也就是说，除了SIGCHILD这个例外，信号处理器在显式重置（比如将处理器设置为SIG_DEL以
            恢复默认行为，或设置为SIG_IGN以忽略信号）之前一直保持设置状态。SIGCHID行为是平台各
            异的
        signal.pause:
            使进程休眠，直到捕捉到下一个信号。调用time.sleep也可以达到这个目的。

    """
    signum = int(sys.argv[2])
    signal.signal(signum, on_signal)
    while True:
        signal.pause()


def on_signal_main2():
    print('Setting at', now())
    signal.signal(signal.SIGALRM, on_signal())
    signal.alarm(5)
    signal.pause()


if __name__ == '__main__':
    eval(sys.argv[1])()
