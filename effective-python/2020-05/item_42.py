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
class MyObject:
    def __init__(self):
        self.public_field = 5
        self.__private_field = 10

    def get_private_field(self):
        return self.__private_field


example(2)
foo = MyObject()
assert foo.public_field == 5


example(3)
assert foo.get_private_field() == 10


example(4)
try:
    foo.__private_field
except:
    logging.exception('Expected')
else:
    assert False


example(5)
class MyOtherObject:
    def __init__(self):
        self.__private_field = 71

    @classmethod
    def get_private_field_of_instance(cls, instance):
        return instance.__private_field

bar = MyOtherObject()
assert MyOtherObject.get_private_field_of_instance(bar) == 71


example(6)
try:
    class MyParentObject:
        def __init__(self):
            self.__private_field = 71
    
    class MyChildObject(MyParentObject):
        def get_private_field(self):
            return self.__private_field
    
    baz = MyChildObject()
    baz.get_private_field()
except:
    logging.exception('Expected')
else:
    assert False


example(7)
assert baz._MyParentObject__private_field == 71


example(8)
print(baz.__dict__)


example(9)
class MyStringClass:
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return str(self.__value)

foo = MyStringClass(5)
assert foo.get_value() == '5'


example(10)
class MyIntegerSubclass(MyStringClass):
    def get_value(self):
        return int(self._MyStringClass__value)

foo = MyIntegerSubclass('5')
assert foo.get_value() == 5


example(11)
class MyBaseClass:
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

class MyStringClass(MyBaseClass):
    def get_value(self):
        return str(super().get_value())         # Updated

class MyIntegerSubclass(MyStringClass):
    def get_value(self):
        return int(self._MyStringClass__value)  # Not updated


example(12)
try:
    foo = MyIntegerSubclass(5)
    foo.get_value()
except:
    logging.exception('Expected')
else:
    assert False


example(13)
class MyStringClass:
    def __init__(self, value):
        # This stores the user-supplied value for the object.
        # It should be coercible to a string. Once assigned in
        # the object it should be treated as immutable.
        self._value = value


    def get_value(self):
        return str(self._value)
class MyIntegerSubclass(MyStringClass):
    def get_value(self):
        return self._value

foo = MyIntegerSubclass(5)
assert foo.get_value() == 5


example(14)
class ApiClass:
    def __init__(self):
        self._value = 5

    def get(self):
        return self._value

class Child(ApiClass):
    def __init__(self):
        super().__init__()
        self._value = 'hello'  # Conflicts

a = Child()
print(f'{a.get()} and {a._value} should be different')


example(15)
class ApiClass:
    def __init__(self):
        self.__value = 5       # Double underscore

    def get(self):
        return self.__value    # Double underscore

class Child(ApiClass):
    def __init__(self):
        super().__init__()
        self._value = 'hello'  # OK!

a = Child()
print(f'{a.get()} and {a._value} are different')
