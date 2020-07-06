import zipfile

# 读取
example_zip = zipfile.ZipFile('example.zip')
example_zip.namelist()

# 创建
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt')
newZip.close()

# -l:显示zip格式压缩包中的文件列表
# -c:创建zip格式压缩包
# -e:提取zip格式压缩包
# -t:验证文件是一个有效的zip格式研所包
# python -m zipfile -c monty.zip spam.txt eggs.txt
# python -m zipfile -e monty.zip target-dir


file = zipfile.ZipFile('temp.zip')
file.extractall(pwd='error')

with open('passwords.txt') as pf:
    for line in pf:
        try:
            file.extractall(pwd=line.strip())
            print("password is {0}".format(line.strip()))
        except:
            pass


