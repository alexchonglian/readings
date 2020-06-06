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
try:
    class MyError(Exception):
        pass
    
    def my_generator():
        yield 1
        yield 2
        yield 3
    
    it = my_generator()
    print(next(it))  # Yield 1
    print(next(it))  # Yield 2
    print(it.throw(MyError('test error')))
except:
    logging.exception('Expected')
else:
    assert False


example(2)
def my_generator():
    yield 1
    try:
        yield 2
    except MyError:
        print('Got MyError!')
        #yield 2.5
    else:
        yield 3
    yield 4
    yield 5

it = my_generator()
print(next(it))  # Yield 1
print(next(it))  # Yield 2
print(it.throw(MyError('test error')))


example(3)
class Reset(Exception):
    pass

def timer(period):
    current = period
    while current:
        current -= 1
        try:
            yield current
        except Reset:
            current = period


example(4)
RESETS = [
    False, False, False, True, False, True, False,
    False, False, False, False, False, False, False]

def check_for_reset():
    # Poll for external event
    return RESETS.pop(0)

def announce(remaining):
    print(f'{remaining} ticks remaining')

def run():
    it = timer(4)    
    while True:
        try:
            if check_for_reset():
                current = it.throw(Reset())
            else:
                current = next(it)
        except StopIteration:
            break
        else:
            announce(current)

run()


example(5)
class Timer:
    def __init__(self, period):
        self.current = period
        self.period = period

    def reset(self):
        self.current = self.period

    def __iter__(self):
        while self.current:
            self.current -= 1
            yield self.current


example(6)
RESETS = [
    False, False, True, False, True, False,
    False, False, False, False, False, False, False]

def run():
    timer = Timer(4)
    for current in timer:
        if check_for_reset():
            timer.reset()
        announce(current)

run()
