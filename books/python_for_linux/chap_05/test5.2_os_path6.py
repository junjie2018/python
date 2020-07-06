# ！/usr/bin/python
from __future__ import print_function

import os

os.chdir(os.path.expanduser('~'))
print([item for item in os.listdir(os.path.expanduser('~')) if os.path.isfile(item)])
print([item for item in os.listdir(os.path.expanduser('~')) if os.path.isdir(item)])
print({item: os.path.realpath(item) for item in os.listdir(os.path.expanduser('~')) if os.path.isdir(item)})
print({item: os.path.getsize(item) for item in os.listdir(os.path.expanduser('~')) if os.path.isfile(item)})
