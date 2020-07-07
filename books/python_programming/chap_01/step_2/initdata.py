bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 30000, 'job': 'dev'}
tom = {'name': 'Tom', 'age': 50, 'pay': 0, 'job': None}

db = dict(bob=bob, sue=sue, tom=tom)

if __name__ == '__main__':
    for key in db:
        print(key, '=>\n', db[key])
