from __future__ import print_function

with open('data.txt') as inf:
    for line in inf:
        print(line.upper())

with open('data.txt') as inf, open('data5.txt', 'w') as outf:
    for line in inf:
        outf.write(" ".join([word.capitalize() for word in line.split()]))
        outf.write("\n")

# 这儿的*号是什么意思
with open('data.txt') as inf, open('data6.txt', 'w') as outf:
    for line in inf:
        print(*[word.capitalize() for word in line.split()], file=outf)
