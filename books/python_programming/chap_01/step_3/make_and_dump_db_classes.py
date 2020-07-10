import shelve

from books.python_programming.chap_01.step_3.person_alternative import Person
from books.python_programming.chap_01.step_3.person_alternative import Manager


def generate():
    bob = Person('Bob Smith', 42, 30000, 'software')
    sue = Person('Sue Jones', 45, 40000, 'hardware')
    tom = Manager('Tol Doe', 50, 50000)

    db = shelve.open('class-shelve')
    db['bob'] = bob
    db['sue'] = sue
    db['tom'] = tom
    db.close()


def dump():
    db = shelve.open('class-shelve')
    for key in db:
        print(key, '=>\n ', db[key].name, db[key].pay)


def update():
    db = shelve.open('class-shelve')
    sue = db['sue']
    sue.give_raise(.25)
    db['sue'] = sue

    tom = db['tom']
    tom.give_raise(.20)
    db['tom'] = tom
    db.close()


def main():
    generate()
    # dump()
    # update()
    # dump()


if __name__ == '__main__':
    main()
