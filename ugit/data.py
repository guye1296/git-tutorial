import os
import hashlib

GIT_DIR = '.ugit'
OBJECTS_DIR = os.path.join(GIT_DIR, 'objects')


def init():
    os.makedirs(GIT_DIR)
    os.makedirs(OBJECTS_DIR)


def hash_object(data) -> str:
    oid = hashlib.sha1(data).hexdigest()
    with open(os.path.join(OBJECTS_DIR, oid), 'wb') as out:
        out.write(data)
    return oid


def cat_file(object_name) -> bytes:
    with open(os.path.join(OBJECTS_DIR, object_name), 'rb') as object_data:
        return object_data.read()

