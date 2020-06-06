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
for i in range(3):
    print('Loop', i)
else:
    print('Else block')

example(2)
for i in range(3):
    print('Loop', i)
    if i == 1:
        break
else:
    print('Else block!')


example(3)
for x in []:
    print('Never runs')
else:
    print('For Else block!')


example(4)
while False:
    print('Never runs')
else:
    print('While Else block!')

#The rationale for these behaviors is that
# else blocks after loops are useful
# when using loops to search for something.

example(5)
a = 4
b = 9
for i in range(2, min(a, b)+1):
    print('Testing', i)
    if a%i == 0 and b%i == 0:
        print('not coprime')
        break
else:
    print('coprime')

example(6)
def coprime(a, b):
    for i in range(2, min(a, b)+1):
        if a%i == 0 and b%i == 0:
            return False
    return True

print(coprime(4, 9))
print(coprime(3, 6))

example(7)
def coprime(a, b):
    is_coprime = True
    for i in range(2, min(a, b)+1):
        if a%i == 0 and b%i == 0:
            is_coprime = False
            break
    return is_coprime

print(coprime(4, 9))
print(coprime(3, 6))




