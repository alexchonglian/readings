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
stock = {
    'nails': 125,
    'screws': 35,
    'wingnuts': 8,
    'washers': 24,
}

order = ['screws', 'wingnuts', 'clips']

def get_batches(count, size):
    return count // size

result = {}
for name in order:
  count = stock.get(name, 0)
  batches = get_batches(count, 8)
  if batches:
    result[name] = batches

print(result)


example(2)
found = {name: get_batches(stock.get(name, 0), 8)
         for name in order
         if get_batches(stock.get(name, 0), 8)}
print(found)


example(3)
has_bug = {name: get_batches(stock.get(name, 0), 4)
           for name in order
           if get_batches(stock.get(name, 0), 8)}

print('Expected:', found)
print('Found:   ', has_bug)


example(4)
found = {name: batches for name in order
         if (batches := get_batches(stock.get(name, 0), 8))}
assert found == {'screws': 4, 'wingnuts': 1}, found


example(5)
try:
    result = {name: (tenth := count // 10)
              for name, count in stock.items() if tenth > 0}
except:
    logging.exception('Expected')
else:
    assert False


example(6)
result = {name: tenth for name, count in stock.items()
          if (tenth := count // 10) > 0}
print(result)


example(7)
half = [(last := count // 2) for count in stock.values()]
print(f'Last item of {half} is {last}')


example(8)
for count in stock.values():  # Leaks loop variable
    pass
print(f'Last item of {list(stock.values())} is {count}')


example(9)
try:
    del count
    half = [count // 2 for count in stock.values()]
    print(half)   # Works
    print(count)  # Exception because loop variable didn't leak
except:
    logging.exception('Expected')
else:
    assert False


example(10)
found = ((name, batches) for name in order
         if (batches := get_batches(stock.get(name, 0), 8)))
print(next(found))
print(next(found))
