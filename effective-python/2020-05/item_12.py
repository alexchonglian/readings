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
x = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = x[::2]
evens = x[1::2]
print(odds)
print(evens)


example(2)
x = b'mongoose'
y = x[::-1]
print(y)


example(3)
x = '寿司'
y = x[::-1]
print(y)


example(4)
try:
    w = '寿司'
    x = w.encode('utf-8')
    y = x[::-1]
    z = y.decode('utf-8')
except:
    logging.exception('Expected')
else:
    assert False


example(5)
x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
x[::2]   # ['a', 'c', 'e', 'g']
x[::-2]  # ['h', 'f', 'd', 'b']


example(6)
x[2::2]     # ['c', 'e', 'g']
x[-2::-2]   # ['g', 'e', 'c', 'a']
x[-2:2:-2]  # ['g', 'e']
x[2:2:-2]   # []


example(7)
y = x[::2]   # ['a', 'c', 'e', 'g']
z = y[1:-1]  # ['c', 'e']
print(x)
print(y)
print(z)
