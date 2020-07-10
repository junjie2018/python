import sys
import traceback

print(sys.platform)
print(sys.maxsize)
print(sys.version)
if sys.platform[:3] == 'win': print('hello windows')

print(sys.modules)
print(list(sys.modules.keys()))
print(sys)
print(sys.modules['sys'])
print(sys.getrefcount(sys))  # 这样的么
print(sys.builtin_module_names)

try:
    raise IndexError
except:
    print(sys.exc_info())


def grail(x):
    raise TypeError('already got one')


try:
    grail('arthur')
except:
    exc_info = sys.exc_info()
    print(exc_info[0])
    print(exc_info[1])
    traceback.print_tb(exc_info[2])
