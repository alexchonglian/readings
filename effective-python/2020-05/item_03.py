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
a = b'h\x65llo'
print(list(a))
print(a)

print(list('hello'))
print([ord(c) for c in 'hello'])

example(2)
a = 'a\u0300 propos'
print(list(a))
print(a)

example(3)
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value

print(repr(to_str(b'foo')))
print(repr(to_str(u'foo')))
print(repr(to_str( 'foo')))
print(type(b'foo'))
print(type(u'foo'))
print(type( 'foo'))


example(4)
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value

print(repr(to_bytes(b'foo')))
print(repr(to_bytes(u'foo')))
print(repr(to_bytes( 'foo')))

example(15)
try:
    with open('data.bin', 'w') as f:
        f.write(b'\xf1\xf2\xf3\xf4\xf5')
except:
    logging.exception('Expected')
else:
    assert False



example(17)

try:
    real_open = open
    def open(*args, **kwargs):
        kwargs['encoding'] = 'utf-8'
        return real_open(*args, **kwargs)

    with open('data.bin', 'r') as f:
        data = f.read()
except:
    logging.exception('Expected')


open = real_open


