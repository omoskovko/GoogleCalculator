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

print(ExampleSibling.__mro__)

'''
# OutPut is like following
(<class '__main__.ExampleSibling'>, <class '__main__.Example'>, <class '__main__.MyObject'>, <class '__main__.Sibling'>, <class '__main__.MyType'>, <class 'type'>, <class 'object'>)
'''
