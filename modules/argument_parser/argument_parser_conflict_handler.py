import argparse

# case 1
# parser = argparse.ArgumentParser(prog='PROG')
# parser.add_argument('-f', '--foo', help='old foo help')
# parser.add_argument('--foo', help='new foo help')

# case 2
parser = argparse.ArgumentParser(prog='PROG', conflict_handler='resolve')
parser.add_argument('-f', '--foo', help='old foo help')
parser.add_argument('--foo', help='new foo help')
parser.print_help()
