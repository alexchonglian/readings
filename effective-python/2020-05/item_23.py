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
def remainder(number, divisor):
    return number % divisor

assert remainder(20, 7) == 6


example(2)
remainder(20, 7)
remainder(20, divisor=7)
remainder(number=20, divisor=7)
remainder(divisor=7, number=20)


example(3)
try:
    # This will not compile
    source = """remainder(number=20, 7)"""
    eval(source)
except:
    logging.exception('Expected')
else:
    assert False


example(4)
try:
    remainder(20, number=7)
except:
    logging.exception('Expected')
else:
    assert False


example(5)
my_kwargs = {
    'number': 20,
    'divisor': 7,
}
assert remainder(**my_kwargs) == 6


example(6)
my_kwargs = {
    'divisor': 7,
}
assert remainder(number=20, **my_kwargs) == 6


example(7)
my_kwargs = {
    'number': 20,
}
other_kwargs = {
    'divisor': 7,
}
assert remainder(**my_kwargs, **other_kwargs) == 6


example(8)
def print_parameters(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')

print_parameters(alpha=1.5, beta=9, gamma=4)


example(9)
def flow_rate(weight_diff, time_diff):
    return weight_diff / time_diff

weight_diff = 0.5
time_diff = 3
flow = flow_rate(weight_diff, time_diff)
print(f'{flow:.3} kg per second')


example(10)
def flow_rate(weight_diff, time_diff, period):
    return (weight_diff / time_diff) * period


example(11)
flow_per_second = flow_rate(weight_diff, time_diff, 1)


example(12)
def flow_rate(weight_diff, time_diff, period=1):
    return (weight_diff / time_diff) * period


example(13)
flow_per_second = flow_rate(weight_diff, time_diff)
flow_per_hour = flow_rate(weight_diff, time_diff, period=3600)
print(flow_per_second)
print(flow_per_hour)


example(14)
def flow_rate(weight_diff, time_diff,
              period=1, units_per_kg=1):
    return ((weight_diff * units_per_kg) / time_diff) * period


example(15)
pounds_per_hour = flow_rate(weight_diff, time_diff,
                            period=3600, units_per_kg=2.2)
print(pounds_per_hour)


example(16)
pounds_per_hour = flow_rate(weight_diff, time_diff, 3600, 2.2)
print(pounds_per_hour)
