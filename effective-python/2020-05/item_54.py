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
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self, offset):
        self.count += offset


example(2)
def worker(sensor_index, how_many, counter):
    # I have a barrier in here so the workers synchronize
    # when they start counting, otherwise it's hard to get a race
    # because the overhead of starting a thread is high.
    BARRIER.wait()
    for _ in range(how_many):
        # Read from the sensor
        # Nothing actually happens here, but this is where
        # the blocking I/O would go.
        counter.increment(1)


example(3)
from threading import Barrier
BARRIER = Barrier(5)
from threading import Thread

how_many = 10**5
counter = Counter()

threads = [Thread(target=worker, args=(i, how_many, counter)) \
    for i in range(5)]
for thread in threads: thread.start()
for thread in threads: thread.join()

expected = how_many * 5
found = counter.count
print(f'Counter should be {expected}, got {found}')


example(4)
counter.count += 1


example(5)
value = getattr(counter, 'count')
result = value + 1
setattr(counter, 'count', result)


example(6)
# Running in Thread A
value_a = getattr(counter, 'count')
# Context switch to Thread B
value_b = getattr(counter, 'count')
result_b = value_b + 1
setattr(counter, 'count', result_b)
# Context switch back to Thread A
result_a = value_a + 1
setattr(counter, 'count', result_a)


example(7)
from threading import Lock

class LockingCounter:
    def __init__(self):
        self.lock = Lock()
        self.count = 0

    def increment(self, offset):
        with self.lock:
            self.count += offset


example(8)
BARRIER = Barrier(5)
counter = LockingCounter()

threads = [Thread(target=worker, args=(i, how_many, counter)) \
    for i in range(5)]
for thread in threads: thread.start()
for thread in threads: thread.join()

expected = how_many * 5
found = counter.count
print(f'Counter should be {expected}, got {found}')
