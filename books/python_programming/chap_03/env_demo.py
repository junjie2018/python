import os
import sys


# print(os.environ.keys())
# print(list(os.environ.keys()))
# print(os.environ['TEMP'])
#
# print(os.environ['PYTHONPATH'])
# for srcdir in os.environ['PYTHONPATH'].split(os.pathsep):
#     print(srcdir)
#
# print(sys.path[:3])
#
# print(os.environ['TEMP'])
# os.environ['TEMP'] = r'c:\temp'
# print(os.environ['TEMP'])

"""
    在最新版本的Python，赋给os.environ的键值将自动被导出到应用的其他部分。
    即复制将同时改变Python程序中的os.environ对象，以及该进程对应的shell
    环境变量。Python程序、所有链如的C模块，所有该Python进程派生的子程序
    都可以看到新的赋值。
    
    我的理解：
        1.在a shell中运行python进程修改环境变量，并不会影响到a shell本身的环境变量
        2.由a shell运行的python进程派生的进程的环境变量会受到该python进程修改环境变
          量的影响，而且，可能还是实时的。
  
    在内部，对os.environ的键赋值将会调用os.putenv，它负责改变python解释器外部的shell
    变量——我不是很理解这句话，什么叫做改变python解释器外部的shell变量，实际上实验中，
    调用该python脚本的shell中环境变量并没有发生改变。
    
    可以这样理解，shell是一个进程，shell启动的python也是一个进程，修改python解释器外部
    的shell变量就是修改这个python进程的shell。好抽象
    
    
    子程序是有如下方式启动的程序：在Unix下os.spawnv os.fork/exec或者所有平台下的os.popen
    os.system subprocess
"""
def main():
    choice = sys.argv[1]
    if choice == 'display':
        print('Hello, ', os.environ['USER'])
    elif choice == 'set':
        print(os.environ['USER'])
        os.environ['USER'] = 'Brian'
        os.system('python env_demo.py display')
        os.environ['USER'] = 'Arthur'
        os.system('python env_demo.py display')
        os.environ['USER'] = input('?')
        print(os.popen('python env_demo.py display').read())


if __name__ == '__main__':
    main()
