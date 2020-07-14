import glob
import os

# os.popen 我肯定不会选择这种方案
# print(os.popen('dir /B').readlines())
# for line in os.popen('dir /B'):
#     print(line[:-1])
# print([line[:-1] for line in os.popen('dir /B')])
# print(os.popen('dir *.py /B').readlines())
# print(os.popen(r'c:\cywin\bin\ls *.bin').readlines())
# print(list(os.popen(r'dir parts /B')))
# print([fname for fname in os.popen(r'c:\cygwin\bin\ls parts')])
# print(list(os.popen(r'dir parts\part* /B')))
# print(list(os.popen(r'c:/cygwin/bin/ls pargs/part*')))


# glob
"""
    glob调用接收shell中的常用文件名模式语法：？代表任意单个字符，*代表任意个字符，[] 括起来的是字符选集。
    如果你希望glob匹配的文件不在当前工作目录中，那么匹配模式中还应该包括一个目录路径，此外，这个模块可以
    接受Unix或DOS风格的目录分隔符。该调用的实现没有涉及派生shell命令（它使用的是os.listdir）。
    
    glob还有一些特性：事实上，用它来列出目录中的文件只是模式匹配技巧的多用途之一。其还可以同于在多个目录
    下收集匹配名称，因为所传入的目录路径里的每一级都可以是同一个模式。
    
    glob只是利用标准模块fnmatch来匹配名称模式
"""
print(glob.glob('*'))
print(glob.glob('*.py'))
print(glob.glob('data.txt'))
print(glob.glob('../chap_01'))  # 这个很奇怪
print(glob.glob('../chap_01/*'))  # 这个和我期待的是一样的
print(glob.glob('../chap_01/step_*'))
for path in glob.glob('../../*/*.py'): print(path)

# os.listdir
print(os.listdir('.'))
print(os.listdir(os.curdir))
print(os.listdir('..'))

# 总结
print(os.popen('dir /b parts').readlines())
print(glob.glob(r'parts\*'))
print(os.listdir('parts'))
