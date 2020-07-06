import shutil
import tarfile

print(shutil.get_archive_formats())

shutil.make_archive('backup', 'gztar')
shutil.make_archive('backup', 'zip')

# 用tarfile解压
f = tarfile.open('backup.tar.gz', 'r:gz')
print(f.getnames())

# 用shutil解压
shutil.unpack_archive('backup.tar.gz')
