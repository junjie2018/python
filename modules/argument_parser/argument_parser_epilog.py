import argparse

# case 1
parser = argparse.ArgumentParser(
    description='A foo that bars',
    epilog="And that's how you'd foo a bar")
parser.print_help()
