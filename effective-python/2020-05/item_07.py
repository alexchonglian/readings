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
from random import randint
random_bits = 0
for i in range(32):
    if randint(0, 1):
        random_bits |= 1 << i
print(bin(random_bits))


example(2)
flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for flavor in flavor_list:
    print(f'{flavor} is delicious')


example(3)
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print(f'{i + 1}: {flavor}')


example(4)
it = enumerate(flavor_list)
print(next(it))
print(next(it))


example(5)
for i, flavor in enumerate(flavor_list):
    print(f'{i + 1}: {flavor}')


example(6)
for i, flavor in enumerate(flavor_list, 1):
    print(f'{i}: {flavor}')
