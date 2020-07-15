import argparse

# argument_default=SUPPRESS：没有传递相应参数时就不创建对应的属性
parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
# parser = argparse.ArgumentParser()
parser.add_argument('--foo')
parser.add_argument('bar', nargs='?')
print(parser.parse_args(['--foo', '1', 'BAR']))

print(parser.parse_args([]))
