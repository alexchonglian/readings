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
class Homework:
    def __init__(self):
        self._grade = 0

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if not (0 <= value <= 100):
            raise ValueError(
                'Grade must be between 0 and 100')
        self._grade = value


example(2)
galileo = Homework()
galileo.grade = 95
assert galileo.grade == 95


example(3)
example(4)
class Exam:
    def __init__(self):
        self._writing_grade = 0
        self._math_grade = 0

    @staticmethod
    def _check_grade(value):
        if not (0 <= value <= 100):
            raise ValueError(
                'Grade must be between 0 and 100')

    @property
    def writing_grade(self):
        return self._writing_grade

    @writing_grade.setter
    def writing_grade(self, value):
        self._check_grade(value)
        self._writing_grade = value

    @property
    def math_grade(self):
        return self._math_grade

    @math_grade.setter
    def math_grade(self, value):
        self._check_grade(value)
        self._math_grade = value

galileo = Exam()
galileo.writing_grade = 85
galileo.math_grade = 99

assert galileo.writing_grade == 85
assert galileo.math_grade == 99


example(5)
class Grade:
    def __get__(self, instance, instance_type):
        pass

    def __set__(self, instance, value):
        pass

class Exam:
    # Class attributes
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


example(6)
exam = Exam()
exam.writing_grade = 40


example(7)
Exam.__dict__['writing_grade'].__set__(exam, 40)


example(8)
exam.writing_grade


example(9)
Exam.__dict__['writing_grade'].__get__(exam, Exam)


example(10)
class Grade:
    def __init__(self):
        print('init Grade')
        self._value = 0

    def __get__(self, instance, instance_type):
        print(f"__get__({instance}, {instance_type})")
        return self._value

    def __set__(self, instance, value):
        print(f"__set__({instance}, {value})")
        if not (0 <= value <= 100):
            raise ValueError(
                'Grade must be between 0 and 100')
        self._value = value


example(11)
class Exam:
    # class attributes
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()

first_exam = Exam()
first_exam.writing_grade = 82
first_exam.science_grade = 99
print('Writing', first_exam.writing_grade)
print('Science', first_exam.science_grade)


example(12)
second_exam = Exam()
second_exam.writing_grade = 75
print(f'Second Writing {second_exam.writing_grade} is right')
print(f'Second Science {second_exam.science_grade} is the same as First')
print(f'First {first_exam.writing_grade} is wrong; '
      f'should be 82')

example(12.1)
print('Second >>>')
print(1, second_exam.writing_grade)
print(2, Exam.__dict__)
print(3, Exam.__dict__["writing_grade"])
print(4, second_exam.__getattribute__("writing_grade"))
print(5, type(second_exam.__getattribute__("writing_grade")))
print(6, type(second_exam.writing_grade))
print(7, second_exam.science_grade)

example(12.2)
"""
class Exam:
    def __init__(self):
        # instance variables won't work?
        self.math_grade = Grade()
        self.writing_grade = Grade()
        self.science_grade = Grade()

first_exam = Exam()
first_exam.writing_grade = 82
first_exam.science_grade = 99
print('Writing', first_exam.writing_grade)
print('Science', first_exam.science_grade)
second_exam = Exam()
second_exam.writing_grade = 75
print('Second >>>')
print(second_exam.writing_grade)
print(second_exam.__dict__)
print(second_exam.__dict__["writing_grade"])
print(second_exam.__getattribute__("writing_grade"))
print(type(second_exam.writing_grade))
print(second_exam.science_grade)
print(f'First  {first_exam.writing_grade} is correct; '
      f'should be 82')
"""


example(13)
class Grade:
    def __init__(self):
        print('init Grade')
        self._values = {}

    def __get__(self, instance, instance_type):
        print(f"__get__({instance}, {instance_type})")
        if instance is None:
        # grade attribute is access from class? not instalce
            return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        print(f"__set__({instance}, {value})")
        if not (0 <= value <= 100):
            raise ValueError(
                'Grade must be between 0 and 100')
        self._values[instance] = value

exam = Exam()
print(exam.writing_grade) # __get__(object Exam(), class Exam)
print(Exam.writing_grade) # __set__(None,          class Exam)

example(14)
from weakref import WeakKeyDictionary

class Grade:
    def __init__(self):
        print('init Grade')
        self._values = WeakKeyDictionary()

    def __get__(self, instance, instance_type):
        print(f"__get__({instance}, {instance_type})")
        if instance is None:
            return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        print(f"__set__({instance}, {value})")
        if not (0 <= value <= 100):
            raise ValueError(
                'Grade must be between 0 and 100')
        self._values[instance] = value


example(15)
class Exam:
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()

first_exam = Exam()
first_exam.writing_grade = 82
second_exam = Exam()
second_exam.writing_grade = 75
print(f'First  {first_exam.writing_grade} is right')
print(f'Second {second_exam.writing_grade} is right')
