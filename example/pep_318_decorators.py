"""
https://www.python.org/dev/peps/pep-0318/
PEP:	318
Title:	Decorators for Functions and Methods
Author:	Kevin D. Smith <Kevin.Smith at theMorgue.org>, Jim J. Jewett, Skip Montanaro, Anthony Baxter
Status:	Final
Type:	Standards Track
Created:	05-Jun-2003
Python-Version:	2.4
Post-History:	09-Jun-2003, 10-Jun-2003, 27-Feb-2004, 23-Mar-2004, 30-Aug-2004, 2-Sep-2004
"""

"""

Current Syntax

The current syntax for function decorators as implemented in Python 2.4a2 is:

@dec2
@dec1
def func(arg1, arg2, ...):
    pass

This is equivalent to:

def func(arg1, arg2, ...):
    pass
func = dec2(dec1(func))

without the intermediate assignment to the variable func. 
The decorators are near the function declaration. 
The @ sign makes it clear that something new is going on here.

The rationale for the order of application [16] (bottom to top) is that it matches the usual order for function-application. 
In mathematics, composition of functions (g o f)(x) translates to g(f(x)). In Python, @g @f def foo() translates to foo=g(f(foo).

The decorator statement is limited in what it can accept -- arbitrary expressions will not work. 
Guido preferred this because of a gut feeling [17].

The current syntax also allows decorator declarations to call a function that returns a decorator:

@decomaker(argA, argB, ...)
def func(arg1, arg2, ...):
    pass

This is equivalent to:

func = decomaker(argA, argB, ...)(func)

The rationale for having a function that returns a decorator is that the part after the @ sign 
can be considered to be an expression (though syntactically restricted to just a function), 
and whatever that expression returns is called. See declaration arguments [16].
"""

"""
Examples

Much of the discussion on comp.lang.python and the python-dev mailing list focuses on the use of decorators 
as a cleaner way to use the staticmethod() and classmethod() builtins. This capability is much more powerful than that. 
This section presents some examples of use.

    Define a function to be executed at exit. Note that the function isn't actually "wrapped" in the usual sense.
"""


def onexit(f):
    import atexit

    atexit.register(f)
    return f


@onexit
def func():
    print("Exit")


"""
    Note that this example is probably not suitable for real usage, but is for example purposes only.

    Define a class with a singleton instance. Note that once the class disappears enterprising programmers 
    would have to be more creative to create more instances. (From Shane Hathaway on python-dev.)

    def singleton(cls):
        instances = {}
        def getinstance():
            if cls not in instances:
                instances[cls] = cls()
            return instances[cls]
        return getinstance

    @singleton
    class MyClass:
        ...

    Add attributes to a function. (Based on an example posted by Anders Munch on python-dev.)
"""


def attrs(**kwds):
    def decorate(f):
        for k in kwds:
            setattr(f, k, kwds[k])
        return f

    return decorate


@attrs(versionadded="2.2", author="Guido van Rossum")
def mymethod():
    print(mymethod.versionadded)
    print(mymethod.author)


mymethod()

"""
    Enforce function argument and return types. Note that this copies the func_name attribute from the old to the new function. 
    func_name was made writable in Python 2.4a3:
"""


def accepts(*types):
    def check_accepts(f):
        #        assert len(types) == f.__code__.co_argcount
        def new_f(*args, **kwds):
            for a, t in zip(args, types):
                assert isinstance(a, t), "arg %r does not match %s" % (a, t)
            return f(*args, **kwds)

        new_f.__name__ = f.__name__
        return new_f

    return check_accepts


def returns(rtype):
    def check_returns(f):
        def new_f(*args, **kwds):
            result = f(*args, **kwds)
            assert isinstance(result, rtype), "return value %r does not match %s" % (
                result,
                rtype,
            )
            return result

        new_f.__name__ = f.__name__
        return new_f

    return check_returns


@accepts(int, (int, float))
@returns((int, float))
def func(arg1, arg2):
    return arg1 * arg2


print(func(2, 6))
print(func([2], 6))

'''
    Declare that a class implements a particular (set of) interface(s). 
    This is from a posting by Bob Ippolito on python-dev based on experience with PyProtocols [28].

    def provides(*interfaces):
         """
         An actual, working, implementation of provides for
         the current implementation of PyProtocols.  Not
         particularly important for the PEP text.
         """
         def provides(typ):
             declareImplementation(typ, instancesProvide=interfaces)
             return typ
         return provides

    class IBar(Interface):
         """Declare something about IBar here"""

    @provides(IBar)
    class Foo(object):
            """Implement something here..."""
'''
