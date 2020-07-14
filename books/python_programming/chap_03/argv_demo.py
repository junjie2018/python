"""
    getopt模块：仿效Unix/C中的同名工具
    optparse模块：一个新的替代直选，通常任务它的功能更强大（以后研究一下）
        https://docs.python.org/3/library/optparse.html
"""

def getopts(argv):
    opts = {}
    while argv:
        if argv[0][0] == '-':
            opts[argv[0]] = argv[1]
            argv = argv[2:]
        else:
            argv = argv[1:]
    return opts


if __name__ == '__main__':
    from sys import argv

    myargs = getopts(argv)
    if '-i' in myargs:
        print(myargs['-i'])
    print(myargs)
