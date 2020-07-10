import os
import sys

"""
    Shell变量：            os.environ
    运行程序：             os.system, os.popen, os.execv, os.spawnv
    派生进程：             os.fork, os.pipe, os.watipid, os.kill
    文件描述符、文件锁：   os.open, os.read, os.write
    文件处理：             os.remove os.rename os.mkfifo os.mkdir os.rmdir
    管理工具：             os.getcwd os.chdir os.chmod os.getpid os.listdir os.access
    移植工具：             os.set os.pathsep os.curdir os.path.split os.path.join
    路径名工具：            os.path.exists('path') os.path.isdir('path') os.path.getsize('path')
"""

print(os.getpid())

print(os.getcwd())
print(os.chdir(r'C:\Users'))
print(os.getcwd())

print(os.pathsep)
print(os.sep)
print(os.pardir)
print(os.curdir)
print(os.linesep)

print(os.path.split(r'C:\temp\data.txt'))
print(os.path.join(r'C:\temp', 'output.txt'))

# todo 我不知道，为嘛最后的文件名，要叫做basename
name = r'C:\temp\data.txt'
print(os.path.dirname(name))
print(os.path.basename(name))

name = '/home/lutz/temp/data.txt'
print(os.path.dirname(name))
print(os.path.basename(name))

# todo 这个留意下，因为需求少，所以容易忘记
print(os.path.splitext(r'C:\PPRthEd\Examples\PP4E\PyDemos.pyw'))

pathname = r'C:\PPRthEd\Examples\PP4E\PyDemos.pyw'
print(os.sep)
print(os.path.split(pathname))
print(pathname.split(os.sep))
print(os.sep.join(pathname.split(os.sep)))
print(os.path.join(*pathname.split(os.sep)))  # 这个才windows平台表现的的确有问题

print(os.path.isdir(r'C:\Users'), os.path.isfile(r'C:\Users'))
print(os.path.isdir(r'C:\config.sys'), os.path.isfile(r'C:\dell.sdr'))  # 这个要执行一个真实存在的文件
print(os.path.isdir('nonesuch'), os.path.isfile('nonesuch'))

print(os.path.exists(r'c:\Users\Brian'))
print(os.path.exists(r'c:\Users\Default'))
print(os.path.getsize(r'C:\dell.sdr'))

mixed = r'c:\temp\public/files\index.html'
print(os.path.normpath(mixed))
print(os.path.normpath(r'c:\tep\\sub\.\file.ext'))

# 相对os.getcwd()求各个路径
os.chdir(r'c:/users')
print(os.getcwd())
print(os.path.abspath(''))
print(os.path.abspath('temp'))
print(os.path.abspath(r'PP4E\dev'))
print(os.path.abspath('.'))
print(os.path.abspath('..'))
print(os.path.abspath(r'c:\PP4thEd\chapters'))
print(os.path.abspath(r'c:\temp\spam.txt'))

"""
    os.system: 在Python脚本中运行shell命令
    os.popen: 运行shell命令并与其输入输出流相连接
"""
os.chdir(r'D:\python\books\python_programming\chap_02')
os.system('dir .')
os.system('type more.py')
os.system('type temp')

print(open('more.py').read())
print(os.popen('type more.py').read())
print(os.popen('dir .').readlines())

# os.system('python more.py sys_demo.py')  # 可以执行，当前进程
# print(os.popen('python more.py sys_demo.py').read())  # 另一个进程被阻塞了，输入后才能得到输出
print(os.popen('python tmp.py').read())

"""
    os.system函数通常会阻塞（其实是暂停）它的调用者，知道所启动的命令行程序退出。在Linux和
    类Unix平台上，所启动的命令行一般可独立于调用者，与之并行地运行，只需要在命令行代码末尾
    加上shell后台运算符&即可：
        
        os.system("python program.py arg arg &")
    
    在Windows下，用DOS的start命令通常也能是命令并行启动：
    
        os.system("start program.py arg arg")
    
    新近的Python版本中加入了os.startfile函数，这一增加非常有用。这个函数会打开一个文件，无
    论文件的类型是什么，就像用鼠标单击它的图标一样：
    
        os.startfile('webpage.html')
        os.startfile('document.doc')
        os.startfile('myscript.py')
"""
# os.startfile('index.html') # 没有做出实验效果
# os.startfile('tmp.py')
# os.startfile('myscript.py')

"""
    不是很理解这部分

    os.popen函数一般不会阻塞其调动者（根据定义，调用者必须能够读取或写入所返回的文件对象），
    但是无论在Window还是Linux下，如果管道对象在所启动的程序退出前关闭（如进行垃圾回收时），
    或是管道一次性完成读取（如调用read()方法），那么任然有可能阻塞调用者。在这一部分稍后章
    节会看到，Unix的os.fork/exec调用和Windows的os.spawnv调用也可用来不受阻塞困扰地并行运行
    程序。
    
    os模块的system和popen调用，以及subprocess模块也可归为程序启动、流重定向和进程间通信的
    手段。  
"""

"""
    os.environ  ：获取和设置shell环境变量
    os.fork     ：在类Unix系统下派生新的子进程
    os.pipe     ：负责程序间通信
    os.execlp   ：启动新程序
    os.spawnv   ：启动带有底层控制的新程序
    os.open     ：打开基于底层描述符的文件
    os.mkdir    ：创建新目录
    os.mkfifo   ：创建新的命名管道
    os.stat     ：获取文件底层信息
    os.remove   ：根据路径名删除文件
    os.walk     ：将函数或循环应用于这个目录树的各部分
"""
