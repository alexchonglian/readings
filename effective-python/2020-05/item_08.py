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
names = ['Cecilia', 'Lise', 'Marie']
counts = [len(n) for n in names]
print(counts)


example(2)
longest_name = None
max_count = 0
for i in range(len(names)):
    count = counts[i]
    if count > max_count:
        longest_name = names[i]
        max_count = count

print(longest_name)


example(3)
longest_name = None
max_count = 0
for i, name in enumerate(names):
    count = counts[i]
    if count > max_count:
        longest_name = name
        max_count = count
assert longest_name == 'Cecilia'


example(4)
longest_name = None
max_count = 0
for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count
assert longest_name == 'Cecilia'


example(5)
names.append('Rosalind')
for name, count in zip(names, counts):
    print(name)


example(6)
import itertools
for name, count in itertools.zip_longest(names, counts):
    print(f'{name}: {count}')
