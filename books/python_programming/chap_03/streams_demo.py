"""
    当遇到文件结束符时input将抛出一个异常，然而文件read方法只返回一个空串。因为input会脱去
    每行的行结束符，一个空串以为这空行，所以我们需要用异常来处理文件结束符。文件read方法保
    持行结束符并将空行指示为“\n”而非空串。这是使用sys.stdin和input的一点区别。

"""

"""
    一段有趣的论证：
        more.py错误地使用stdin：以方便它通过调用input从stdin读取用户的交互输入，另一方面它从stdin中读取
        输入文本。当stdin流重定向到文件或换到时，我们无法再用它读取用户交互输入，此时它只能获取输入源的
        文本。而且，stdin在程序启动时就被重定向，因此无法获取重定向前的标准输入流。
    
    要实现在stdin接收输入并利用console作为用户交互，需要使用特殊的接口从键盘而非标准输入，直接读取用户输入。
    在Windows下，Python标准库msvcrt模块提供了该功能；在类Unix平台上，可以读取设备文件/dev/tty

"""
import sys
from io import StringIO
from io import BytesIO


# 已经理解上文描述的所有内容了
def more(text, numlines=15):
    lines = text.splitlines()
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk:
            print(line)
        if lines and input("More?") not in ['y', 'Y']:
            break


def getreply():
    if sys.stdin.isatty():
        return input('?')
    else:
        if sys.platform[:3] == 'win':
            import msvcrt
            msvcrt.putch(b"?")
            key = msvcrt.getche()
            msvcrt.putch(b'\n')
            return key
        else:
            # 这个还没有接触到
            assert False, 'platform not support'
            # linux?: open('/dev/tty').readline()[:1]


def more2(text, numlines=10):
    lines = text.splitlines()
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk:
            print(line)
        if lines and getreply() not in ['y', 'Y']:
            break


def more_run():
    if len(sys.argv) == 2:
        more(sys.stdin.read())
    else:
        more(open(sys.argv[2], encoding="utf-8").read())


def more2_run():
    print(len(sys.argv))
    if len(sys.argv) == 2:
        more2(sys.stdin.read())
    else:
        more(open(sys.argv[2], encoding="utf-8").read())


def hello():
    print('hello stdout world')
    sys.stdout.write('hello stdout world \n')
    input('hello stdio world>')  # 读取的值并没有使用到
    print('hello stdio wordl>')  # 仅仅只是一个提示
    print(sys.stdin.readline())  # 读取一行标准输入


def interact():
    print('Hello stream world')
    while True:
        try:
            reply = input('Enter a number>')
        except EOFError:
            break
        else:
            num = int(reply)
            print("%d squared is %d" % (num, num ** 2))
    print('Bye')


def sorter_small():
    for line in sorted(sys.stdin): print(line, end='')


def adder_small():
    print(sum(int(line) for line in sys.stdin))


def reader():
    print('Got this: "%s"' % input())
    data = sys.stdin.readline()[:-1]
    print('The meaning of life is', data, int(data) * 2)


def writer():
    print("Help! Help! I'm being repressed!")
    print(42)


def writer2():
    for data in (123, 0, 999, 42):
        print("%03d" % data)


def adder():
    sum = 0
    while True:
        try:
            line = input()
        except EOFError:
            break
        else:
            sum += int(line)
    print(sum)


def adder2():
    sum = 0
    while True:
        line = sys.stdin.readLine()
        if not line: break
        sum += int(line)
    print(sum)


def adder3():
    sum = 0
    for line in sys.stdin: sum += int(line)
    print(sum)


def sorter():
    lines = sys.stdin.readlines()
    lines.sort()
    for line in lines: print(line, end=' ')


def string_io():
    buff = StringIO()
    buff.write('spam\n')
    buff.write('eggs\n')
    print(buff.getvalue())

    buff = StringIO('ham\nspam\n')
    print(buff.readline())
    print(buff.readline())
    print(buff.readline())

    # 将StringIO赋值个sys.stdout
    buff = StringIO()
    temp = sys.stdout
    sys.stdout = buff
    print(42, 'spam', 3.141)
    sys.stdout = temp
    print(buff.getvalue())


def bytes_io():
    stream = BytesIO()
    stream.write(b'spam')
    print(stream.getvalue())

    stream = BytesIO(b'dpam')
    print(stream.read())


class Output:
    def __init__(self):
        self.text = ''

    def write(self, string):
        self.text += string

    def writelines(self, lines):
        for line in lines:
            self.write(line)


class Input:
    def __init__(self, input=''):
        self.text = input

    def read(self, size=None):
        if size is None:
            res, self.text = self.text, ''
        else:
            res, self.text = self.text[:size], self.text[size:]
        return res

    def readline(self):
        eoln = self.text.find('\n')
        if eoln == -1:
            res, self.text = self.text, ''
        else:
            res, self.text = self.text[:eoln + 1], self.text[eoln + 1:]
        return res


def redirect(function, pargs, kargs, input):
    savestreams = sys.stdin, sys.stdout
    sys.stdin = Input(input)
    sys.stdout = Output()
    try:
        result = function(*pargs, **kargs)
        output = sys.stdout.text
    finally:
        sys.stdin, sys.stdout = savestreams
    return result, output


def output_input_test():
    (result, output) = redirect(interact, (), {}, '4\n5\n5\n')
    print(result)
    print(output)


def main():
    choice = sys.argv[1]

    eval(choice)()


if __name__ == '__main__':
    main()
