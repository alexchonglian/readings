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
a = 0b10111011
b = 0xc5f
print('Binary is %d, hex is %d' % (a, b))


example(2)
key = 'my_var'
value = 1.234
formatted = '%-10s = %.2f' % (key, value)
print(formatted)


example(3)
try:
    reordered_tuple = '%-10s = %.2f' % (value, key)
except:
    logging.exception('Expected')
else:
    assert False


example(4)
try:
    reordered_string = '%.2f = %-10s' % (key, value)
except:
    logging.exception('Expected')
else:
    assert False


example(5)
pantry = [
    ('avocados', 1.25),
    ('bananas', 2.5),
    ('cherries', 15),
]
for i, (item, count) in enumerate(pantry):
    print('#%d: %-10s = %.2f' % (i, item, count))

example(6)
for i, (item, count) in enumerate(pantry):
    print('#%d: %-10s = %d' % (
        i + 1,
        item.title(),
        round(count)))

example(7)
template = '%s loves food. See %s cook.'
name = 'Max'
formatted = template % (name, name)
print(formatted)


example(8)
name = 'brad'
formatted = template % (name.title(), name.title())
print(formatted)


example(9)
key = 'my_var'
value = 1.234
old_way = '%-10s = %.2f' % (key, value)
new_way = '%(key)-10s = %(value).2f' % {
    'key': key, 'value': value}  # Original
reordered = '%(key)-10s = %(value).2f' % {
    'value': value, 'key': key}  # Swapped
print(old_way)
print(new_way)
print(reordered)
assert old_way == new_way == reordered

example(10)
name = 'Max'

template = '%s loves food. See %s cook.'
before = template % (name, name)   # Tuple
template = '%(name)s loves food. See %(name)s cook.'
after = template % {'name':name}
assert before == after

example(11)
for i, (item, count) in enumerate(pantry):
    before = '#%d: %-10s = %d' % (
        i + 1,
        item.title(),
        round(count))

    after = '#%(loop)d: %(item)-10s = %(count)d' % {
        'loop': i + 1,
        'item': item.title(),
        'count': round(count),
    }

    assert before == after


example(12)
soup = 'lentil'
formatted = 'Today\'s soup is %(soup)s.' % {'soup': soup}
print(formatted)


example(13)
menu = {
    'soup': 'lentil',
    'oyster': 'kumamoto',
    'special': 'schnitzel',
}
template = ('Today\'s soup is %(soup)s, '
            'buy one get two %(oyster)s oysters, '
            'and our special entrée is %(special)s.')
formatted = template % menu
print(formatted)

example(14)
a = 1234.5678
formatted = format(a, ',.2f')
print(formatted)

b = 'my string'
formatted = format(b, '^20s')
print('*', formatted, '*')

example(15)
key = 'my_var'
value = 1.234

formatted = '{} = {}'.format(key, value)
print(formatted)

example(16)
formatted = '{:10} == {:.2f}'.format(key, value)
print(formatted)

example(17)
# escaping % and {}
print('%.2f%%' % 12.5)
print('{} replaces {{}}'.format(1.23))

example(18)
# positional
formatted = '{1} = {0}'.format(key, value)
print(formatted)

example(19)
formatted = '{0} loves food. See {0} cook.'.format(name)
print(formatted)


example(20)
for i, (item, count) in enumerate(pantry):
    old_style = '#%d: %-10s = %d' % (
        i + 1,
        item.title(),
        round(count))

    new_style = '#{}: {:<10s} = {}'.format(
        i + 1,
        item.title(),
        round(count))

    assert old_style == new_style

example(21)
formatted = 'First letter is {menu[oyster][0]!r}'.format(
    menu=menu)
print(formatted)

example(22)
old_template = (
    'Today\'s soup is %(soup)s, '
    'buy one get two %(oyster)s oysters, '
    'and our special entrée is %(special)s.')
old_formatted = template % {
    'soup': 'lentil',
    'oyster': 'kumamoto',
    'special': 'schnitzel',
}

new_template = (
    'Today\'s soup is {soup}, '
    'buy one get two {oyster} oysters, '
    'and our special entrée is {special}.')
new_formatted = new_template.format(
    soup='lentil',
    oyster='kumamoto',
    special='schnitzel',
)

example(23)
key = 'my_var'
value = 1.234

formatted = f'{key} = {value}'
print(formatted)

example(24)
formatted = f'{key!r:<10} = {value:.2f}'
print(formatted)

example(25)
f_string = f'{key:<10} = {value:.2f}'
c_tuple  = '%-10s = %.2f' % (key, value)
c_dict   = '%(key)-10s = %(value).2f' % {'key': key, 'value': value}
str_args = '{:<10} = {:.2f}'.format(key, value)
str_kw   = '{key:<10} = {value:.2f}'.format(key=key, value=value)

assert len({f_string, c_tuple, c_dict, str_args, str_kw}) == 1


example(26)
for i, (item, count) in enumerate(pantry):
    old_style = '#%d: %-10s = %d' % (
        i + 1,
        item.title(),
        round(count))

    new_style = '#{}: {:<10s} = {}'.format(
        i + 1,
        item.title(),
        round(count))

    f_string = f'#{i+1}: {item.title():<10s} = {round(count)}'

    assert old_style == new_style == f_string

example(27)
for i, (item, count) in enumerate(pantry):
    print(f'#{i+1}: '
          f'{item.title():<10s} = '
          f'{round(count)}')

example(28)
places = 3
number = 1.23456
print(f'My number is {number:.{places}f}')
