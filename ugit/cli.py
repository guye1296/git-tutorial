import argparse
import os
from . import data


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    commands = parser.add_subparsers(dest='command')
    commands.required = True

    init_parser = commands.add_parser('init')
    init_parser.set_defaults(func=init)

    return parser.parse_args()


def init(args):
    print(f"initialized emtpty ugit repository in {os.path.join(os.getcwd(), data.GIT_DIR)}")
    return data.init()


def main():
    args = parse_args()
    args.func(args)

