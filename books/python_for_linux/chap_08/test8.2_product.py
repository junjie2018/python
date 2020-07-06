from itertools import product

l1 = ('a', 'b', 'c')
l2 = (22, 80)

# 方式一
list([(x, y) for x in l1 for y in l2])

# 方式二
list(product(l1, l2))
