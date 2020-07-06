#!/usr/bin/python
import os
import fnmatch


def is_file_match(filename, patterns):
    for pattern in patterns:
        if fnmatch.fnmatch(filename, pattern):
            return True
    return False


def find_specific_files(root, patterns=['*'], exclude_dirs=[]):
    for root, dirnames, filenames in os.walk(root):
        for filename in filenames:
            if is_file_match(filename, patterns):
                yield os.path.join(root, filename)
        for d in exclude_dirs:
            if d in dirnames:
                dirnames.remove(d)


for item in find_specific_files("."):
    print(item)

patterns = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
for item in find_specific_files(".", patterns):
    print(item)

patterns = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
exclude_dirs = ['dir2']
for item in find_specific_files(".", patterns, exclude_dirs):
    print(item)

# python的lambda不是很熟
files = {name: os.path.getsize(name) for name in find_specific_files('.')}
result = sorted(files.items(), key=lambda d: d[1], reverse=True)[:10]
for i, t in enumerate(result, 1):
    print(i, t[0], t[1])

# 找到10个最大的文件
files = {name: os.path.getsize(name) for name in find_specific_files('.', exclude_dirs=['.git'])}
result = sorted(files.items(), key=lambda d: d[1], reverse=True)[:10]
for i, t in enumerate(result, 1):
    print(i, t[0], t[1])

# 找到10个最老的文件
files = {name: os.path.getmtime(name) for name in find_specific_files('.')}
result = sorted(files.items(), key=lambda d: d[1])[:10]
for i, t in enumerate(result, 1):
    print(i, t[0], t[1])

# 包含mysql-bin的文件
files = [name for name in find_specific_files('.', patterns=['*mysql-bin'])]
for i, name in enumerate(files, 1):
    print(i, name)

# 排除.git子目录以后所有的Python源文件
files = [name for name in find_specific_files('.', patterns=['*mysql-bin'], exclude_dirs=['.git'])]
for i, name in enumerate(files, 1):
    print(i, name)

# 删除某个目录及其子目录下所有的pyc文件
files = [name for name in find_specific_files('.', patterns=['*pyc'])]
for name in files:
    os.remove(name)
