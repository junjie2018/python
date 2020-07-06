import hashlib

md5 = hashlib.md5()

with open('/etc/passwd') as f:
    for line in f:
        md5.update(line)

print(md5.hexdigest)
