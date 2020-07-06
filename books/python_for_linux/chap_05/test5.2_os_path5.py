# ！/usr/bin/python
from __future__ import print_function

import os

file = "data.txt"

print(os.path.getatime(file))
print(os.path.getmtime(file))
print(os.path.getctime(file))
print(os.path.getsize(file))
