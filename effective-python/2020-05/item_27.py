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
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = []
for x in a:
    squares.append(x**2)
print(squares)


example(2)
squares = [x**2 for x in a]  # List comprehension
print(squares)


example(3)
alt = map(lambda x: x ** 2, a)
assert list(alt) == squares, f'{alt} {squares}'


example(4)
even_squares = [x**2 for x in a if x % 2 == 0]
print(even_squares)


example(5)
alt = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
assert even_squares == list(alt)


example(6)
even_squares_dict = {x: x**2 for x in a if x % 2 == 0}
threes_cubed_set = {x**3 for x in a if x % 3 == 0}
print(even_squares_dict)
print(threes_cubed_set)


example(7)
alt_dict = dict(map(lambda x: (x, x**2),
                filter(lambda x: x % 2 == 0, a)))
alt_set = set(map(lambda x: x**3,
              filter(lambda x: x % 3 == 0, a)))
assert even_squares_dict == alt_dict
assert threes_cubed_set == alt_set
