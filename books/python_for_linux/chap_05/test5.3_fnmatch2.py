import os
import fnmatch

print(os.listdir('.'))
print([name for name in os.listdir('.') if fnmatch.fnmatch(name, '*.jpg')])
print([name for name in os.listdir('.') if fnmatch.fnmatch(name, '[a-z]*')])
print([name for name in os.listdir('.') if fnmatch.fnmatch(name, '[a-z]*.txt')])
print([name for name in os.listdir('.') if fnmatch.fnmatch(name, '[!a-d]*')])
print([name for name in os.listdir('.') if fnmatch.fnmatch(name, '[!a-d]*')])