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
class Meta(type):
    def __new__(meta, name, bases, class_dict):
        global print
        orig_print = print
        print(f'* Running {meta}.__new__ for {name}')
        print('Bases:', bases)
        print = pprint
        print(class_dict)        
        print = orig_print
        return type.__new__(meta, name, bases, class_dict)

class MyClass(metaclass=Meta):
    stuff = 123

    def foo(self):
        pass

class MySubclass(MyClass):
    other = 567

    def bar(self):
        pass

mysubclass = MySubclass()
print('MyClass: ', MyClass.__dict__)
print('MySubclass: ', MySubclass.__dict__)
print(MySubclass.__mro__)
print(mysubclass.__dict__)
print(type(mysubclass).__mro__)


example(2)
class ValidatePolygon(type):
    def __new__(meta, name, bases, class_dict):
        # Only validate subclasses of the Polygon class
        if bases:
            if class_dict['sides'] < 3:
                raise ValueError('Polygons need 3+ sides')
        return type.__new__(meta, name, bases, class_dict)

class Polygon(metaclass=ValidatePolygon):
    sides = None  # Must be specified by subclasses

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180

class Triangle(Polygon):
    sides = 3

class Rectangle(Polygon):
    sides = 4

class Nonagon(Polygon):
    sides = 9

assert Triangle.interior_angles() == 180
assert Rectangle.interior_angles() == 360
assert Nonagon.interior_angles() == 1260


example(3)
try:
    print('Before class')
    
    class Line(Polygon):
        print('Before sides')
        sides = 2
        print('After sides')
    
    print('After class')
except:
    logging.exception('Expected')
else:
    assert False


example(4)
class BetterPolygon:
    sides = None  # Must be specified by subclasses

    def __init_subclass__(cls):
        super().__init_subclass__()
        if cls.sides < 3:
            raise ValueError('Polygons need 3+ sides')  

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180

class Hexagon(BetterPolygon):
    sides = 6

assert Hexagon.interior_angles() == 720


example(5)
try:
    print('Before class')
    
    class Point(BetterPolygon):
        sides = 1
    
    print('After class')
except:
    logging.exception('Expected')
else:
    assert False


example(6)
class ValidateFilled(type):
    def __new__(meta, name, bases, class_dict):
        # Only validate subclasses of the Filled class
        if bases:
            if class_dict['color'] not in ('red', 'green'):
                raise ValueError('Fill color must be supported')
        return type.__new__(meta, name, bases, class_dict)

class Filled(metaclass=ValidateFilled):
    color = None  # Must be specified by subclasses


example(7)
try:
    class RedPentagon(Filled, Polygon):
        color = 'blue'
        sides = 5
except:
    logging.exception('Expected')
else:
    assert False


example(8)
class ValidatePolygon(type):
    def __new__(meta, name, bases, class_dict):
        # Only validate non-root classes
        if not class_dict.get('is_root'):
            if class_dict['sides'] < 3:
                raise ValueError('Polygons need 3+ sides')
        return type.__new__(meta, name, bases, class_dict)

class Polygon(metaclass=ValidatePolygon):
    is_root = True
    sides = None  # Must be specified by subclasses

class ValidateFilledPolygon(ValidatePolygon):
    def __new__(meta, name, bases, class_dict):
        # Only validate non-root classes
        if not class_dict.get('is_root'):
            if class_dict['color'] not in ('red', 'green'):
                raise ValueError('Fill color must be supported')
        return super().__new__(meta, name, bases, class_dict)

class FilledPolygon(Polygon, metaclass=ValidateFilledPolygon):
    is_root = True
    color = None  # Must be specified by subclasses


example(9)
class GreenPentagon(FilledPolygon):
    color = 'green'
    sides = 5

greenie = GreenPentagon()
assert isinstance(greenie, Polygon)


example(10)
try:
    class OrangePentagon(FilledPolygon):
        color = 'orange'
        sides = 5
except:
    logging.exception('Expected')
else:
    assert False


example(11)
try:
    class RedLine(FilledPolygon):
        color = 'red'
        sides = 2
except:
    logging.exception('Expected')
else:
    assert False


example(12)
class Filled:
    color = None  # Must be specified by subclasses

    def __init_subclass__(cls):
        super().__init_subclass__()
        if cls.color not in ('red', 'green', 'blue'):
            raise ValueError('Fills need a valid color')  


example(13)
class RedTriangle(Filled, Polygon):
    color = 'red'
    sides = 3

ruddy = RedTriangle()
assert isinstance(ruddy, Filled)
assert isinstance(ruddy, Polygon)


example(14)
try:
    print('Before class')
    
    class BlueLine(Filled, Polygon):
        color = 'blue'
        sides = 2
    
    print('After class')
except:
    logging.exception('Expected')
else:
    assert False


example(15)
try:
    print('Before class')
    
    class BeigeSquare(Filled, Polygon):
        color = 'beige'
        sides = 4
    
    print('After class')
except:
    logging.exception('Expected')
else:
    assert False


example(16)
class Top:
    def __init_subclass__(cls):
        super().__init_subclass__()
        print(f'Top for {cls}')

class Left(Top):
    def __init_subclass__(cls):
        super().__init_subclass__()
        print(f'Left for {cls}')

class Right(Top):
    def __init_subclass__(cls):
        super().__init_subclass__()
        print(f'Right for {cls}')

class Bottom(Left, Right):
    def __init_subclass__(cls):
        super().__init_subclass__()
        print(f'Bottom for {cls}')

print(Bottom.__mro__)
