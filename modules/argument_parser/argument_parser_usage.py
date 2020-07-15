import argparse

"""
    我目前推断:
        -打头的就是option arguments，非-打头的就是position arguments
        nargs='+' 
            positional：一个或多个
            optional  ：该操作的阐述一个或多个
        nargs='?' 
            positional：参数零个或者一个
            optional  ：该操作执行一次或多次
"""

# case 1
# parser = argparse.ArgumentParser(prog='PROG')
# parser.add_argument('--foo', nargs='+', help='foo help')
# parser.add_argument('bar', nargs='+', help='bar help')
# args = parser.parse_args()

# case 2
parser = argparse.ArgumentParser(prog='PROG', usage='%(prog)s [optional]')
parser.add_argument('--foo', nargs='+', help='foo help')
parser.add_argument('bar', nargs='+', help='bar help')
args = parser.parse_args()
