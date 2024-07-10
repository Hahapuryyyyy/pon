import sys

import argparse

def create_parser():
    perser = argparse
    perser.add_argument('-n', '--file', default='text')
    return parser
if __name__ == "__main__":
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    print(namespace)
    file = open(f'{namespace.file}.txt', 'r')
    print(file.readlines())














