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
numbers = [93, 86, 11, 68, 70]
numbers.sort()
print(numbers)


example(2)
class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'Tool({self.name!r}, {self.weight})'

tools = [
    Tool('level', 3.5),
    Tool('hammer', 1.25),
    Tool('screwdriver', 0.5),
    Tool('chisel', 0.25),
]


example(3)
try:
    tools.sort()
except:
    logging.exception('Expected')
else:
    assert False


example(4)
print('Unsorted:', repr(tools))
tools.sort(key=lambda x: x.name)
print('\nSorted:  ', tools)


example(5)
tools.sort(key=lambda x: x.weight)
print('By weight:', tools)


example(6)
places = ['home', 'work', 'New York', 'Paris']
places.sort()
print('Case sensitive:  ', places)
places.sort(key=lambda x: x.lower())
print('Case insensitive:', places)


example(7)
power_tools = [
    Tool('drill', 4),
    Tool('circular saw', 5),
    Tool('jackhammer', 40),
    Tool('sander', 4),
]


example(8)
saw = (5, 'circular saw')
jackhammer = (40, 'jackhammer')
assert not (jackhammer < saw)  # Matches expectations


example(9)
drill = (4, 'drill')
sander = (4, 'sander')
assert drill[0] == sander[0]  # Same weight
assert drill[1] < sander[1]   # Alphabetically less
assert drill < sander         # Thus, drill comes first


example(10)
power_tools.sort(key=lambda x: (x.weight, x.name))
print(power_tools)


example(11)
power_tools.sort(key=lambda x: (x.weight, x.name),
                 reverse=True)  # Makes all criteria descending
print(power_tools)


example(12)
power_tools.sort(key=lambda x: (-x.weight, x.name))
print(power_tools)


example(13)
try:
    power_tools.sort(key=lambda x: (x.weight, -x.name),
                     reverse=True)
except:
    logging.exception('Expected')
else:
    assert False


example(14)
power_tools.sort(key=lambda x: x.name)   # Name ascending

power_tools.sort(key=lambda x: x.weight, # Weight descending
                 reverse=True)

print(power_tools)


example(15)
power_tools.sort(key=lambda x: x.name)
print(power_tools)


example(16)
power_tools.sort(key=lambda x: x.weight,
                 reverse=True)
print(power_tools)
