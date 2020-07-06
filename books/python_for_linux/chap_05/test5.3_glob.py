import glob

print(glob.glob("*.txt"))
print(glob.glob("[a-c]?.txt"))
print(glob.glob("[!a-c]?.txt"))
print(glob.glob('tmp+.jpg'))
