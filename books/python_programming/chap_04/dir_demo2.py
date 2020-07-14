import glob, sys
import os

dirname_main = r'D:\python\books\python_programming'


def glob_test():
    for file in glob.glob(dirname_main + '/**'):
        head, tail = os.path.split(file)
        print(head, tail)


def listdir_test():
    for file in os.listdir(dirname_main):
        print(dirname_main, file, '=>', os.path.join(dirname_main, file))


# 我喜欢这个东西
def walk_test1():
    for (dirname, subshere, fileshere) in os.walk(dirname_main):
        print('[' + dirname + ']')
        for fname in fileshere:
            print(os.path.join(dirname, fname))


def walk_test2():
    matches = []
    for (dirname, dirshere, fileshere) in os.walk(dirname_main):
        for filename in fileshere:
            if filename.endwith('.py'):
                pathname = os.path.join(dirname, filename)
                if 'mimetypes' in open(pathname).read():
                    matches.append(pathname)
    for name in matches: print(name)


def walk_test3(currdir):
    print('[' + currdir + ']')
    for file in os.listdir(currdir):
        path = os.path.join(currdir, file)
        if not os.path.isdir(path):
            print(path)
        else:
            walk_test3(path)


def unicode_test():
    """
        文件名可以包含任意文本，所以3.x中的os.listdir以两种模式运行：如果给定的是bytes参数，
        那么函数将以编码好的字节字符串形式运行文件名；如果给定的是普通的str字符串参数，那么
        它返回的文件名是Unicode字符串，而这个字符串已经根据文件系统的编码体系做过解码了

        在二进制模式下打开文本文件，就意味着原始文本与仍处于编码形式的文本将不会如逾期的那样
        匹配搜索字符串：搜索字符串也必选根据特定且可能不兼容的编码体系编码过的字节字符串。这
        中方法其实就是模仿了python 2.x版本中文本文件的行为，它也突出了为什么在3.x版本中提升
        Unicode的地位是有意的。这样一来，有一部分本来无法处理的文本文件也能够出来的。另一方
        面，如果你不想跳过不可解码且内容大部分都不相关的文件，那么在二进制模式下打开文本文件
        以避免Unicode内容解码和解码错误的做法任然有效。

        作为经验原则，如果编码名称不在系统默认值里，那么你应该总试着为文本内容提供一个编码名
        称，而且在大多数情况下，你应该依赖文件名的默认Unicode API。
    """
    print(os.listdir('.'))
    print(os.listdir(b'.'))

    for (dir, subs, files) in os.walk(dirname_main): print(dir)
    for (dir, subs, files) in os.walk(dirname_main.encode()): print(dir)

    print(glob.glob('.\*'))
    print(glob.glob(b'.\*'))

    print(sys.getdefaultencoding())
    print(sys.getfilesystemencoding())


if __name__ == '__main__':
    eval(sys.argv[1])()
