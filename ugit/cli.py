import argparse
import os
import sys
from . import data


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    commands = parser.add_subparsers(dest='command')
    commands.required = True

    init_parser = commands.add_parser('init')
    init_parser.set_defaults(func=init)

    hash_object_parser = commands.add_parser('hash_object')
    hash_object_parser.set_defaults(func=hash_object)
    hash_object_parser.add_argument('file')

    cat_file_parser = commands.add_parser('cat-file')
    cat_file_parser.set_defaults(func=cat_file)
    cat_file_parser.add_argument('object')

    return parser.parse_args()


def init(args):
    print(f"initialized emtpty ugit repository in {os.path.join(os.getcwd(), data.GIT_DIR)}")
    return data.init()


def hash_object(args):
    with open(args.file, 'rb') as file:
        print(data.hash_object(file.read()))


def cat_file(args):
    object_data = data.cat_file(args.object)
    sys.stdout.buffer.write(object_data)
    sys.stdout.flush()


def main():
    args = parse_args()
    args.func(args)

