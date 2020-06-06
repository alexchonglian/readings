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
def normalize(numbers):
    total = sum(numbers)
    return [100*n/total for n in numbers]

example(2)
visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)
assert sum(percentages) == 100.0

example(3)
path = 'my_numbers.txt'
with open(path, 'w') as f:
    for i in (15, 35, 80):
        f.write('%d\n' % i)

def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


example(4)
it = read_visits('my_numbers.txt')
percentages = normalize(it)
print(percentages)


example(5)
it = read_visits('my_numbers.txt')
print(list(it))
print(list(it))  # Already exhausted


example(6)
def normalize_copy(numbers):
    numbers_copy = list(numbers)  # Copy the iterator
    total = sum(numbers_copy)
    return [100 * value / total for value in numbers_copy]


example(7)
it = read_visits('my_numbers.txt')
percentages = normalize_copy(it)
print(percentages)
assert sum(percentages) == 100.0


example(8)
def normalize_func(get_iter):
    total = sum(get_iter())   # New iterator
    return [100 * value / total for value in get_iter()]  # New iterator


example(9)
path = 'my_numbers.txt'
percentages = normalize_func(lambda: read_visits(path))
print(percentages)
assert sum(percentages) == 100.0


example(10)
class ReadVisits:
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


example(11)
visits = ReadVisits(path)
percentages = normalize(visits)
print(percentages)
assert sum(percentages) == 100.0


example(12)
def normalize_defensive(numbers):
    if iter(numbers) is numbers:  # An iterator -- bad!
        raise TypeError('Must supply a container')
    total = sum(numbers)
    return [100 * value / total for value in numbers]

visits = [15, 35, 80]
normalize_defensive(visits)  # No error

it = iter(visits)
try:
    normalize_defensive(it)
except TypeError:
    pass
else:
    assert False


example(13)
from collections.abc import Iterator 

def normalize_defensive(numbers):
    if isinstance(numbers, Iterator):  # Another way to check
        raise TypeError('Must supply a container')
    total = sum(numbers)
    return [100 * value / total for value in numbers]

visits = [15, 35, 80]
normalize_defensive(visits)  # No error

it = iter(visits)
try:
    normalize_defensive(it)
except TypeError:
    pass
else:
    assert False


example(14)
visits = [15, 35, 80]
percentages = normalize_defensive(visits)
assert sum(percentages) == 100.0

visits = ReadVisits(path)
percentages = normalize_defensive(visits)
assert sum(percentages) == 100.0


example(15)
try:
    visits = [15, 35, 80]
    it = iter(visits)
    normalize_defensive(it)
except:
    logging.exception('Expected')
else:
    assert False
