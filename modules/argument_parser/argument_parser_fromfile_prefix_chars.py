import argparse

# case 1
parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
parser.add_argument('-f')
parser.add_argument('-b')
print(parser.parse_args(['@args.txt', '@args2.txt']))
