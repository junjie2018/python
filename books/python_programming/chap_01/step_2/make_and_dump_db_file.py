import os

dbfilename = 'people-file'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'


def storeDbase(db, dbfilename=dbfilename):
    """将数据库格式化保存为普通文件"""
    dbfile = open(dbfilename, 'w')
    for key in db:
        print(key, file=dbfile)
        for (name, value) in db[key].items():
            print(name + RECSEP + repr(value), file=dbfile)
        print(ENDREC, file=dbfile)
    print(ENDDB, file=dbfile)
    dbfile.close()


def loadDbase(dbfilename=dbfilename):
    """解析数据，重新构建数据库"""
    dbfile = open(dbfilename)
    import sys
    sys.stdin = dbfile
    db = {}
    key = input()
    while key != ENDDB:
        rec = {}
        field = input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = eval(value)
            field = input()
        db[key] = rec
        key = input()
    return db


def generate():
    from books.python_programming.chap_01.step_2.initdata import db
    storeDbase(db)


def update():
    db = loadDbase()
    db['sue']['pay'] *= 1.10
    db['tom']['name'] = 'Tom Tom'
    storeDbase(db)


def dump():
    db = loadDbase()

    for key in db:
        print(key, '=>\n', db[key])
    print(db['sue']['name'])


def main():
    if not os.path.exists('people-file'):
        generate()
    dump()
    update()
    dump()


if __name__ == '__main__':
    main()
