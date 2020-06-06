import random
random.seed(1234)

import logging
from pprint import pprint
from sys import stdout as STDOUT

# Write all output to a temporary directory
import atexit
import gc
import io
import os
import tempfile

TEST_DIR = tempfile.TemporaryDirectory()
atexit.register(TEST_DIR.cleanup)

# Make sure Windows processes exit cleanly
OLD_CWD = os.getcwd()
atexit.register(lambda: os.chdir(OLD_CWD))
os.chdir(TEST_DIR.name)

def close_open_files():
    everything = gc.get_objects()
    for obj in everything:
        if isinstance(obj, io.IOBase):
            obj.close()

atexit.register(close_open_files)

def example(i): print(f'\n==== Example {i} ====')

example(1)
pictures = {}
path = 'profile_1234.png'

with open(path, 'wb') as f:
    f.write(b'image data here 1234')

if (handle := pictures.get(path)) is None:
    try:
        handle = open(path, 'a+b')
    except OSError:
        print(f'Failed to open path {path}')
        raise
    else:
        pictures[path] = handle

handle.seek(0)
image_data = handle.read()

print(pictures)
print(image_data)


example(2)
# Examples using in and KeyError
pictures = {}
path = 'profile_9991.png'

with open(path, 'wb') as f:
    f.write(b'image data here 9991')

if path in pictures:
    handle = pictures[path]
else:
    try:
        handle = open(path, 'a+b')
    except OSError:
        print(f'Failed to open path {path}')
        raise
    else:
        pictures[path] = handle

handle.seek(0)
image_data = handle.read()

print(pictures)
print(image_data)

pictures = {}
path = 'profile_9922.png'

with open(path, 'wb') as f:
    f.write(b'image data here 9991')

try:
    handle = pictures[path]
except KeyError:
    try:
        handle = open(path, 'a+b')
    except OSError:
        print(f'Failed to open path {path}')
        raise
    else:
        pictures[path] = handle

handle.seek(0)
image_data = handle.read()

print(pictures)
print(image_data)


example(3)
pictures = {}
path = 'profile_9239.png'

with open(path, 'wb') as f:
    f.write(b'image data here 9239')

try:
    handle = pictures.setdefault(path, open(path, 'a+b'))
except OSError:
    print(f'Failed to open path {path}')
    raise
else:
    handle.seek(0)
    image_data = handle.read()

print(pictures)
print(image_data)


example(4)
try:
    path = 'profile_4555.csv'
    
    with open(path, 'wb') as f:
        f.write(b'image data here 9239')
    
    from collections import defaultdict

    def open_picture(profile_path):
        try:
            return open(profile_path, 'a+b')
        except OSError:
            print(f'Failed to open path {profile_path}')
            raise

    pictures = defaultdict(open_picture)
    handle = pictures[path] # can't use path as arg to open_picture
    handle.seek(0)
    image_data = handle.read()
except:
    logging.exception('Expected')
else:
    assert False


example(5)
path = 'account_9090.csv'

with open(path, 'wb') as f:
    f.write(b'image data here 9090')

def open_picture(profile_path):
    try:
        return open(profile_path, 'a+b')
    except OSError:
        print(f'Failed to open path {profile_path}')
        raise

class Pictures(dict):
    def __missing__(self, key):
        value = open_picture(key)
        self[key] = value
        return value

pictures = Pictures()
handle = pictures[path]
handle.seek(0)
image_data = handle.read()
print(pictures)
print(image_data)
