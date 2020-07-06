import json

numbers = [1, 2, 3, 4, 5]

filename = 'C:\\Users\\Junjie\\Desktop\\python\\chap_10\\numbers.json'
# with open(filename, 'w') as f_obj:
#     json.dump(numbers, f_obj)

with open(filename, 'w') as f_obj:
    numbers2=json.load(f_obj)
print(numbers2)
