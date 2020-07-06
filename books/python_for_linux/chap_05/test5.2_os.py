# ！/usr/bin/python
from __future__ import print_function

import os

print(os.getcwd())
print(os.chdir(os.path.expanduser('~')))
print(os.getcwd())
