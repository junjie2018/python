import tarfile

with tarfile.open('tarfile_add.tar') as t:
    for member_info in t.getmember():
        print(member_info.name)

with tarfile.open('tarfile_add.tar', mode='w') as out:
    out.add('README.txt')

with tarfile.open('tarfile_add.tar', mode='r:gz') as t:
    for member_info in t.getmember():
        print(member_info.name)

with tarfile.open('tarfile_add.tar', mode='w:gz') as out:
    out.add('README.txt')
