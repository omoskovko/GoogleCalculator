class MyType(type):
    pass

class MyObject(object):
    pass

class NoneSample(MyObject):
    pass

class Example(MyObject):
    pass

class Sibling(MyType):
    pass

class ExampleSibling(Example, Sibling):
    pass

class ExSibngNSample(Example, Sibling, NoneSample):
    pass

print(ExampleSibling.__mro__)
print(ExSibngNSample.__mro__)

'''
# OutPut is like following
(<class '__main__.ExampleSibling'>, <class '__main__.Example'>, <class '__main__.MyObject'>, <class '__main__.Sibling'>, <class '__main__.MyType'>, <class 'type'>, <class 'object'>)
(<class '__main__.ExSibngNSample'>, <class '__main__.Example'>, <class '__main__.Sibling'>, <class '__main__.MyType'>, <class 'type'>, <class '__main__.NoneSample'>, <class '__main__.MyObject'>, <class 'object'>)
'''
