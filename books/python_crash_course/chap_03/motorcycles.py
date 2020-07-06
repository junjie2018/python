motorcycles = ['honda','yamha','suzuki']
print(motorcycles)

# 修改列表中的元素
motorcycles[0]='ducati'
print(motorcycles)

# 向列表中添加元素
motorcycles.append('ducati')
print(motorcycles)

# 向列表中插入元素
motorcycles.insert(0,'ducati')
print(motorcycles)

# 使用del删除元素
del motorcycles[0]
print(motorcycles)

# 使用pop删除值
motorcycles = ['honda','yamha','suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# 使用pop删除列表中任何位置的元素
motorcycles = ['honda','yamha','suzuki']
print(motorcycles)

first_owned=motorcycles.pop(0)
print('The first motorycle I owned was a ' + first_owned.title()+ '.')

# 使用remove根据值删除元素
motorcycles = ['honda','yamha','suzuki']
print(motorcycles)

motorcycles.remove('yamha')
print(motorcycles)