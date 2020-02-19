class X(object):
    base = object

    @classmethod
    def __class_getitem__(cls, base):
        if cls.base == base:
            # makes normal use of class possible
            return cls
        elif isinstance(base, tuple):
            name = '{0}[{1}]'.format(cls.__name__, ", ".join([b.__name__ for b in base]))
            cls_t = base + (cls,)
            return type(name, cls_t, {'base': base})
        else:
            # construct a new type using the given base class and also remember the attribute for future instantiations
            name = f'{cls.__name__}[{base.__name__}]'
            return type(name, (base, cls), {'base': base})


    def f(self):
        raise NotImplementedError()


class X1(X):
    def f(self):
        return 'X1'


class X2(X):
    def __init__(self):
        # use the attribute here to get the right base for the other subclass
        #self.x1 = X1[self.base]()
        pass

    def f(self):
        return super().f() + 'X2'


class X3(X):
    def f(self):
        return super().f()+'X3'

# just the wanted new functionality
class Y(X):
    def g(self):
        return self.f() + 'Y1'

# demonstration
y = X2[X1, Y]()
print(type(y).__mro__)
print(y.g())     # X1X2Y1

x1 = Y[X3, X1]()
print(type(x1).__mro__)
print(x1.g())     # X1Y1

'''
print(y.x1.g())  # X1Y1
print(type(y))   # <class '__main__.X2[Y]'>

# the existing functionality also still works
x = X2()
print(x.f())     # X1X2
print(x.x1.f())  # X1
print(type(x))   # <class '__main__.X2'>
'''