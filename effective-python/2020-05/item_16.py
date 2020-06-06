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
counters = {
    'pumpernickel': 2,
    'sourdough': 1,
}


example(2)
key = 'wheat'

if key in counters:
    count = counters[key]
else:
    count = 0

counters[key] = count + 1

print(counters)


example(3)
key = 'brioche'

try:
    count = counters[key]
except KeyError:
    count = 0

counters[key] = count + 1

print(counters)


example(4)
key = 'multigrain'

count = counters.get(key, 0)
counters[key] = count + 1

print(counters)


example(5)
key = 'baguette'

if key not in counters:
    counters[key] = 0
counters[key] += 1

key = 'ciabatta'

if key in counters:
    counters[key] += 1
else:
    counters[key] = 1

key = 'ciabatta'

try:
    counters[key] += 1
except KeyError:
    counters[key] = 1

print(counters)


example(6)
votes = {
    'baguette': ['Bob', 'Alice'],
    'ciabatta': ['Coco', 'Deb'],
}

key = 'brioche'
who = 'Elmer'

if key in votes:
    names = votes[key]
else:
    votes[key] = names = []

names.append(who)
print(votes)


example(7)
key = 'rye'
who = 'Felix'

try:
    names = votes[key]
except KeyError:
    votes[key] = names = []

names.append(who)

print(votes)


example(8)
key = 'wheat'
who = 'Gertrude'

names = votes.get(key)
if names is None:
    votes[key] = names = []

names.append(who)

print(votes)


example(9)
key = 'brioche'
who = 'Hugh'

if (names := votes.get(key)) is None:
    votes[key] = names = []

names.append(who)

print(votes)


example(10)
key = 'cornbread'
who = 'Kirk'

names = votes.setdefault(key, [])
names.append(who)

print(votes)


example(11)
data = {}
key = 'foo'
value = []
data.setdefault(key, value)
print('Before:', data)
value.append('hello')
print('After: ', data)


example(12)
key = 'dutch crunch'

count = counters.setdefault(key, 0)
counters[key] = count + 1

print(counters)
