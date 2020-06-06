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
class LazyRecord:
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = f'Value for {name}'
        setattr(self, name, value)
        return value


example(2)
data = LazyRecord()
print('Before:', data.__dict__)
print('foo:   ', data.foo)
print('After: ', data.__dict__)


example(3)
class LoggingLazyRecord(LazyRecord):
    def __getattr__(self, name):
        print(f'* Called __getattr__({name!r}), '
              f'populating instance dictionary')
        result = super().__getattr__(name)
        print(f'* Returning {result!r}')
        return result

data = LoggingLazyRecord()
print('exists:     ', data.exists)
print('First foo:  ', data.foo)
print('Second foo: ', data.foo)


example(4)
class ValidatingRecord:
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, name):
        print(f'* Called __getattribute__({name!r})')
        try:
            value = super().__getattribute__(name)
            print(f'* Found {name!r}, returning {value!r}')
            return value
        except AttributeError:
            value = f'Value for {name}'
            print(f'* Setting {name!r} to {value!r}')
            setattr(self, name, value)
            return value

data = ValidatingRecord()
print('exists:     ', data.exists)
print('First foo:  ', data.foo)
print('Second foo: ', data.foo)


example(5)
try:
    class MissingPropertyRecord:
        def __getattr__(self, name):
            if name == 'bad_name':
                raise AttributeError(f'{name} is missing')
            value = f'Value for {name}'
            setattr(self, name, value)
            return value
    
    data = MissingPropertyRecord()
    assert data.foo == 'Value for foo'  # Test this works
    data.bad_name
except:
    logging.exception('Expected')
else:
    assert False


example(6)
data = LoggingLazyRecord()  # Implements __getattr__
print('Before:         ', data.__dict__)
print('Has first foo:  ', hasattr(data, 'foo'))
print('After:          ', data.__dict__)
print('Has second foo: ', hasattr(data, 'foo'))


example(7)
data = ValidatingRecord()  # Implements __getattribute__
print('Has first foo:  ', hasattr(data, 'foo'))
print('Has second foo: ', hasattr(data, 'foo'))


example(8)
class SavingRecord:
    def __setattr__(self, name, value):
        # Save some data for the record
        pass
        super().__setattr__(name, value)


example(9)
class LoggingSavingRecord(SavingRecord):
    def __setattr__(self, name, value):
        print(f'* Called __setattr__({name!r}, {value!r})')
        super().__setattr__(name, value)

data = LoggingSavingRecord()
print('Before: ', data.__dict__)
data.foo = 5
print('After:  ', data.__dict__)
data.foo = 7
print('Finally:', data.__dict__)


example(10)
class BrokenDictionaryRecord:
    def __init__(self, data):
        self._data = {}

    def __getattribute__(self, name):
        print(f'* Called __getattribute__({name!r})')
        return self._data[name]


example(11)
orig_print = print
# don't want to print entire page of "* Called __getattribute__"
def print(*args):pass
try:
    data = BrokenDictionaryRecord({'foo': 3})
    data.foo
except:
    logging.exception('Expected')
else:
    assert False

print = orig_print


example(12)
class DictionaryRecord:
    def __init__(self, data):
        self._data = data

    def __getattribute__(self, name):
        # Prevent weird interactions with isinstance() used
        # by example code harness.
        if name == '__class__':
            return DictionaryRecord
        print(f'* Called __getattribute__({name!r})')
        data_dict = super().__getattribute__('_data')
        return data_dict[name]

data = DictionaryRecord({'foo': 3})
print('foo: ', data.foo)
