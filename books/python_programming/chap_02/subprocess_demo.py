import os
import subprocess

subprocess.call('python tmp.py')
subprocess.call('cmd /C "type tmp.py"')
subprocess.call('type tmp.py', shell=True)

"""
    在类Unix平台上，当shell设置为False时，程序命令行直接由os.execvp运行，这个调用
    我们会在第5张遇到。如果这个参数是True，那么程序将转而由shell运行，而且你还可以
    借助其他参数来指定shell。
"""

# 用communicate来运行命令，并接收它的标准输出流和错误流文本
pipe = subprocess.Popen('python tmp.py', stdout=subprocess.PIPE)
print(pipe.communicate())
print(pipe.returncode)

# 用其他接口直接读取命令的标准输出流，然后等待命令退出
pipe = subprocess.Popen('python tmp.py', stdout=subprocess.PIPE)
print(pipe.stdout.read())
pipe.wait()

print(subprocess.Popen('python tmp.py', stdout=subprocess.PIPE).communicate()[0])
print(os.popen('python tmp.py').read())
