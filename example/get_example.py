import pdb
from time import time

class cached_propert(object):
    '''
          Data descriptors with __set__() and __get__() defined always override 
          a redefinition in an instance dictionary. 
          In contrast, non-data descriptors can be overridden by instances.
          https://docs.python.org/3/reference/datamodel.html#descriptor-invocation
    '''
    def __init__(self, func=None):
        self.func = func
        if not func is None:
           self.__module__ = func.__module__
           self.__name__ = func.__name__

    def __call__(self, func):
        print("__call__")
        if not func is None:
           self.func = func
           self.__module__ = func.__module__
           self.__name__ = func.__name__
        return self

    def __get__(self, instance, owner=None):
        print("__get__")
        if instance is None:
           print("instance is None")
           return self.func(owner)

        name = self.func.__name__
        value = instance.__dict__[name] = self.func(instance)

        return value

class not_cached_propert(cached_propert):
    '''
          Data descriptors with __set__() and __get__() defined always override 
          a redefinition in an instance dictionary. 
          In contrast, non-data descriptors can be overridden by instances.
          https://docs.python.org/3/reference/datamodel.html#descriptor-invocation
    '''
    def __delete__(self, obj):
        print("__delete__")
        obj.__dict__.pop(self.__name__, None)

    def __set__(self, obj, value):
        print("__set__")
        obj.__dict__[self.__name__] = value

class TestCls(object):
    def __init__(self, val):
        self.val = val
        self.test_property = 10
        self.test_property2 = 10

    @cached_propert
    def test_property(self):
        return "Value is '{0}'".format(self.val)

    @not_cached_propert
    def test_property2(self):
        return "Value is '{0}'".format(self.val)

class TestCls2(object):
    def __init__(self, val):
        self.val = val

    @cached_propert()
    def test_property(self):
        try:
            return "Value is '{0}'".format(self.val)
        except AttributeError:
            return "Object is not initialised"

testObj = TestCls(1)
print("-- step 1 ----------------------")
print(testObj.test_property)
print(testObj.test_property2)
print("--------------------------------")

print("-- step 2 ----------------------")
testObj.val = 2
print(testObj.test_property)
print(testObj.test_property2)
print("--------------------------------")

testObj = TestCls2(1)
print("-- step 3 ----------------------")
print(testObj.test_property)
print("--------------------------------")

print("-- step 4 ----------------------")
testObj.val = 2
print(testObj.test_property)
print(TestCls2.test_property)
print("--------------------------------")
