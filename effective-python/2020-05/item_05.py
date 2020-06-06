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
from urllib.parse import parse_qs
my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)
print(repr(my_values))
# {'red': ['5'], 'blue': ['0'], 'green': ['']}

example(2)
print('Red:     ', my_values.get('red'))
print('Green:   ', my_values.get('green'))
print('Blue:    ', my_values.get('blue'))
print('Opacity: ', my_values.get('opacity'))

example(3)
# For query string 'red=5&blue=0&green='
red     = my_values.get('red', [''])[0] or 0
green   = my_values.get('green', [''])[0] or 0
blue    = my_values.get('blue', [''])[0] or 0
opacity = my_values.get('opacity', [''])[0] or 0
print(f'Red:     {red!r}')
print(f'Green:   {green!r}')
print(f'Blue:    {blue!r}')
print(f'Opacity: {opacity!r}')

example(4)
red     = int(my_values.get('red', [''])[0] or 0)
green   = int(my_values.get('green', [''])[0] or 0)
blue    = int(my_values.get('blue', [''])[0] or 0)
opacity = int(my_values.get('opacity', [''])[0] or 0)
print(f'Red:     {red!r}')
print(f'Green:   {green!r}')
print(f'Blue:    {blue!r}')
print(f'Opacity: {opacity!r}')


example(5)
red_str     = my_values.get('red', [''])
green_str   = my_values.get('green', [''])
opacity_str = my_values.get('opacity', [''])
red     = int(red_str[0]) if red_str[0] else 0
green   = int(green_str[0]) if green_str[0] else 0
opacity = int(opacity_str[0]) if opacity_str[0] else 0
print(f'Red:     {red!r}')
print(f'Green:   {green!r}')
print(f'Opacity: {opacity!r}')

example(6)
green_str = my_values.get('green', [''])
if green_str[0]:
    green = int(green_str[0])
else:
    green = 0
print(f'Green:   {green!r}')

example(7)
def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        return int(found[0])
    return default

example(8)
green = get_first_int(my_values, 'green')
print(f'Green:   {green!r}')

