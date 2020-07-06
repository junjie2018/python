import os
import fnmatch

names = os.listdir('.')
print(names)
fnmatch.filter(names, "[a-c]?.txt")
fnmatch.filter(names, "[!a-c]*")
