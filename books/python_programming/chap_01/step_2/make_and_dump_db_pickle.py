import os


def generate():
    from books.python_programming.chap_01.step_2.initdata import db
    import pickle

    dbfile = open('people-pickle', 'wb')
    pickle.dump(db, dbfile)
    dbfile.close()


def dump():
    import pickle
    dbfile = open('people-pickle', 'rb')
    db = pickle.load(dbfile)
    for key in db:
        print(key, '=>\n ', db[key])
    print(db['sue']['name'])


def update():
    import pickle
    dbfile = open('people-pickle', 'rb')
    db = pickle.load(dbfile)
    dbfile.close()

    db['sue']['pay'] *= 1.10
    db['tom']['name'] = 'Tom Tom'

    dbfile = open('people-pickle', 'wb')
    pickle.dump(db, dbfile)
    dbfile.close()


def main():
    if not os.path.exists('people-pickle'):
        generate()
    dump()
    update()
    dump()


if __name__ == '__main__':
    main()
