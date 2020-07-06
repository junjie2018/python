# test input
f = open('data.txt')
print(f.read())
f.close()

# test 2
f = open('data1.txt', 'w')
f.write('hello, world')
f.close()

# test3
# f = open('data1.txt', 'x')
# f = open('data2.txt', 'x')
# f.write('hello, world')
# f.close()


# test4
try:
    f = open('data.txt')
    print(f.read())
finally:
    f.close()

# test5
with open('data.txt') as f:
    print(f.read())
