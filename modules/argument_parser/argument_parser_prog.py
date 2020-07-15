import argparse

# case 1
# parser = argparse.ArgumentParser()
# parser.add_argument('--foo', help='foo help')
# args = parser.parse_args()

# case 2
# parser = argparse.ArgumentParser(prog='myprogram')
# parser.print_help()
# parser.add_argument('--foo', help='foo help')
# args = parser.parse_args()

# case 3
parser = argparse.ArgumentParser(prog='myprogram')
parser.print_help()
parser.add_argument('--foo', help='foo of the %(prog)s program')
args = parser.parse_args()
