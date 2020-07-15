import argparse
import textwrap

# case 1
# parser = argparse.ArgumentParser(
#     prog='PROG',
#     description='''this description
#          was indented weird
#              but that is okay''',
#     epilog='''
#              likewise for this epilog whose whitespace will
#          be cleaned up and whose words will be wrapped
#          across a couple lines''')
# parser.print_help()

# RawDescriptionHelpFormatter这个是个好东西，我非常喜欢
# parser = argparse.ArgumentParser(
#     prog='PROG',
#     formatter_class=argparse.RawDescriptionHelpFormatter,
#     description=textwrap.dedent('''\
#          Please do not mess up this text!
#          --------------------------------
#              I have indented it
#              exactly the way
#              I want it
#          '''))
# parser.print_help()

# case 3
# parser = argparse.ArgumentParser(
#     prog='PROG',
#     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
# parser.add_argument('--foo', type=int, default=42, help='FOO!')
# parser.add_argument('bar', nargs='*', default=[1, 2, 3], help='BAR!')
# parser.print_help()

# case 4
parser = argparse.ArgumentParser(
    prog='PROG',
    formatter_class=argparse.MetavarTypeHelpFormatter)
parser.add_argument('--foo', type=int)
parser.add_argument('bar', type=float)
parser.print_help()
