import shelve
from books.python_programming.chap_01.step_2.initdata import bob, sue, tom


def generate():
    db = shelve.open('people-shelve')
    db['bob'] = bob
    db['sue'] = sue
    db.close()


def dump():
    db = shelve.open('people-shelve')
    for key in db:
        print(key, '=>\n ', db[key])


def update():
    db = shelve.open('people-shelve')
    sue = db['sue']
    sue['pay'] *= 1.50
    db['sue'] = sue
    db['tom'] = tom
    db.close()


def main():
    generate()
    # # dump()
    # update()
    # dump()

if __name__ == '__main__':
    main()
