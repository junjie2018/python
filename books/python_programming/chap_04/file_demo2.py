import os, stat
import sys


class UnknownCommand(Exception):
    pass


def stat_func():
    info = os.stat('data.txt')
    print(info)

    print(info.st_mode)
    print(info.st_size)

    print(info[stat.ST_MODE])
    print(info[stat.ST_SIZE])

    print(stat.S_ISDIR(info.st_mode))
    print(stat.S_ISREG(info.st_mode))


def path_func():
    print(os.path.isdir('data.txt'))
    print(os.path.isfile('data.txt'))
    print(os.path.getsize('data.txt'))


def process_line(line):
    if line[0] == '*':
        print('Ms.', line[1: -1])
    elif line[0] == '+':
        print('Mr.', line[1:-1])
    else:
        raise UnknownCommand(line)


def process_line2(line):
    commands = {'*': 'Ms.', '+': 'Mr.'}
    try:
        print(commands[line[0]], line[1:-1])
    except KeyError:
        raise UnknownCommand(line)


def filter_stream(function):
    for line in sys.stdin:
        print(function(line), end='')


def filter_stream2(function):
    while True:
        line = sys.stdin.readline()
        if not line: break
        print(function(line), end='')


def filter_stream_test():
    filter_stream(lambda line: line)


def filter_files(name, function):
    with open(name, 'r') as input, open(name + '.out', 'w') as output:
        for line in input:
            output.write(function(line))


def filter_files2(name, function):
    input = open(name, 'r')
    output = open(name + '.out', 'w')
    for line in input:
        output.write(function(line))
    input.close()
    output.close()


def scanner(name, function):
    file = open(name, 'r')
    while True:
        line = file.readline()
        if not line: break
        function(line)
    file.close()


def scanner2(name, function):
    list(map(function, open(name, 'r')))


def scanner3(name, function):
    [function(line) for line in open(name, 'r')]


def scanner4(name, function):
    list(function(line) for line in open(name, 'r'))


def scanner5(name, function):
    for line in open(name, 'r'):
        function(line)


def scanner_test():
    scanner('data.txt', process_line)


if __name__ == '__main__':
    eval(sys.argv[1])()
