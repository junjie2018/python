import os

print(os.getcwd())
print(os.path.expanduser('~'))
# 不懂为什么要这样设计
print(os.path.expanduser('~mysql'))
print(os.path.expanduser('~lmx/t'))

print(os.path.abspath('.'))
print(os.path.abspath('..'))
print(os.path.abspath("../t/a.py"))

print(os.path.join('~', 't', 'a.py'))
print(os.path.join(os.path.expanduser('~mysql'), 't', 'a.py'))

print(os.path.isabs('/home/lmx/t/a.py'))
print(os.path.isabs('.'))
