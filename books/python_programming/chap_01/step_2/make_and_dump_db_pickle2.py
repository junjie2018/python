from books.python_programming.chap_01.step_2.initdata import bob, sue, tom
import pickle
import glob


def generate():
    for (key, record) in [('bob', bob), ('tom', tom), ('sue', sue)]:
        recfile = open(key + '.pkl', 'wb')
        pickle.dump(record, recfile)
        recfile.close()


def dump():
    for filename in glob.glob('*pkl'):
        recfile = open(filename, 'rb')
        record = pickle.load(recfile)
        print(filename, '=>\n', record)


def update():
    suefile = open('sue.pkl', 'rb')
    sue = pickle.load(suefile)
    suefile.close()

    sue['pay'] *= 1.10
    suefile = open('sue.pkl', 'wb')
    pickle.dump(sue, suefile)
    suefile.close()


def main():
    # generate()
    # dump()
    update()
    dump()


if __name__ == '__main__':
    main()
