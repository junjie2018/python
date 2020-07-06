import filecmp

filecmp.cmp('a.txt', 'b.txt')
filecmp.cmpfiles('dir1', 'dir2', ['a.txt', 'b.txt', 'c.txt'])

result = filecmp.dircmp('dir1', 'dir2')
result.report()
print(result.left_list)
print(result.left_only)
print(result.right_only)
