import os

GIT_DIR = '.ugit'


def init():
    return os.makedirs(GIT_DIR)
