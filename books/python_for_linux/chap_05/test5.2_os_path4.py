# ！/usr/bin/python
from __future__ import print_function

import os

print("current directory :" + os.getcwd())
path = os.path.abspath(__file__)
print(path)
print(os.path.dirname(path))
print(os.path.pardir)
print(os.path.abspath(os.path.join(os.path.dirname(path), os.path.pardir)))
