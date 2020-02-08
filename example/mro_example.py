class F(object): pass
class E(object): pass
class D(object): pass
class C(D,F): pass
class B(D,E): pass
class A(B,C): pass

'''
https://docs.python.org/3/tutorial/classes.html#multiple-inheritance
9.5.1. Multiple Inheritance

Python supports a form of multiple inheritance as well. A class definition with multiple base classes looks like this:

class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>

For most purposes, in the simplest cases, you can think of the search for attributes inherited from a parent class as depth-first, 
left-to-right, not searching twice in the same class where there is an overlap in the hierarchy. 
Thus, if an attribute is not found in DerivedClassName, it is searched for in Base1, 
then (recursively) in the base classes of Base1, and if it was not found there, it was searched for in Base2, and so on.

In fact, it is slightly more complex than that; the method resolution order changes dynamically to support cooperative calls to super(). 
This approach is known in some other multiple-inheritance languages as call-next-method and is more powerful 
than the super call found in single-inheritance languages.

Dynamic ordering is necessary because all cases of multiple inheritance exhibit one or more diamond relationships 
(where at least one of the parent classes can be accessed through multiple paths from the bottommost class). 
For example, all classes inherit from object, so any case of multiple inheritance provides more than one path to reach object. 
To keep the base classes from being accessed more than once, the dynamic algorithm linearizes the search order in a way that preserves 
the left-to-right ordering specified in each class, that calls each parent only once, and that is monotonic 
(meaning that a class can be subclassed without affecting the precedence order of its parents). 
Taken together, these properties make it possible to design reliable and extensible classes with multiple inheritance. 
For more detail, see https://www.python.org/download/releases/2.3/mro/.

Examples

First example. Consider the following hierarchy:

    >>> O = object
    >>> class F(O): pass
    >>> class E(O): pass
    >>> class D(O): pass
    >>> class C(D,F): pass
    >>> class B(D,E): pass
    >>> class A(B,C): pass

In this case the merge will be as
-------------
CPL[A]=merge([['A'], ['B', 'D', 'E', 'O', 'object'], ['C', 'D', 'F', 'O', 'object'], ['B', 'C']])
-------------
[['A']]=merge([['B', 'D', 'E', 'O', 'object'], ['C', 'D', 'F', 'O', 'object'], ['B', 'C']])
[['A', 'B']]=merge([['D', 'E', 'O', 'object'], ['C', 'D', 'F', 'O', 'object'], ['C']])
[['A', 'B', 'C']]=merge([['D', 'E', 'O', 'object'], ['D', 'F', 'O', 'object']])
[['A', 'B', 'C', 'D']]=merge([['E', 'O', 'object'], ['F', 'O', 'object']])
[['A', 'B', 'C', 'D', 'E']]=merge([['O', 'object'], ['F', 'O', 'object']])
[['A', 'B', 'C', 'D', 'E', 'F']]=merge([['O', 'object'], ['O', 'object']])
[['A', 'B', 'C', 'D', 'E', 'F', 'O']]=merge([['object'], ['object']])
[['A', 'B', 'C', 'D', 'E', 'F', 'O', 'object']]=merge([])

MRO[A]=['A', 'B', 'C', 'D', 'E', 'F', 'O', 'object']

  class.__mro__
    This attribute is a tuple of classes that are considered when looking for base classes during method resolution.
    https://docs.python.org/3/library/stdtypes.html#class.__mro__
'''
print("=>".join([cls.__name__ for cls in A.__mro__]))

''''
# Result is
A=>B=>C=>D=>E=>F=>object
'''

'''
I leave as an exercise for the reader to compute the linearization for my second example:

    >>> O = object
    >>> class F(O): pass
    >>> class E(O): pass
    >>> class D(O): pass
    >>> class C(D,F): pass
    >>> class B(E,D): pass
    >>> class A(B,C): pass

The only difference with the previous example is the change B(D,E) --> B(E,D); 
however even such a little modification completely changes the ordering of the hierarchy

In this case the merge will be as
-------------
CPL[A]=merge([['A'], ['B', 'E', 'D', 'O', 'object'], ['C', 'D', 'F', 'O', 'object'], ['B', 'C']])
-------------
[['A']]=merge([['B', 'E', 'D', 'O', 'object'], ['C', 'D', 'F', 'O', 'object'], ['B', 'C']])
[['A', 'B']]=merge([['E', 'D', 'O', 'object'], ['C', 'D', 'F', 'O', 'object'], ['C']])
[['A', 'B', 'E']]=merge([['D', 'O', 'object'], ['C', 'D', 'F', 'O', 'object'], ['C']])
[['A', 'B', 'E', 'C']]=merge([['D', 'O', 'object'], ['D', 'F', 'O', 'object']])
[['A', 'B', 'E', 'C', 'D']]=merge([['O', 'object'], ['F', 'O', 'object']])
[['A', 'B', 'E', 'C', 'D', 'F']]=merge([['O', 'object'], ['O', 'object']])
[['A', 'B', 'E', 'C', 'D', 'F', 'O']]=merge([['object'], ['object']])
[['A', 'B', 'E', 'C', 'D', 'F', 'O', 'object']]=merge([])

MRO[A]=['A', 'B', 'E', 'C', 'D', 'F', 'O', 'object']

It is enough to invoke the .mro() method of class A:
'''

O = object
class F(O): pass
class E(O): pass
class D(O): pass
class C(D,F): pass
class B(E,D): pass
class A(B,C): pass

print("=>".join([cls.__name__ for cls in A.__mro__]))
'''
# Result is
A=>B=>E=>C=>D=>F=>object
'''

'''
 The following example, originally provided by Samuele Pedroni, shows that the MRO of Python 2.2 is non-monotonic:

    >>> class A(object): pass
    >>> class B(object): pass
    >>> class C(object): pass
    >>> class D(object): pass
    >>> class E(object): pass
    >>> class K1(A,B,C): pass
    >>> class K2(D,B,E): pass
    >>> class K3(D,A):   pass
    >>> class Z(K1,K2,K3): pass

Here are the linearizations according to the C3 MRO (the reader should verify these linearizations as an exercise and draw the inheritance diagram ;-)

    L[A] = A O
    L[B] = B O
    L[C] = C O
    L[D] = D O
    L[E] = E O
    L[K1]= K1 A B C O
    L[K2]= K2 D B E O
    L[K3]= K3 D A O
    L[Z] = Z K1 K2 K3 D A B C E O

-------------
In this case merge will be as following
-------------
CPL[Z]=merge([['Z'], ['K1', 'A', 'B', 'C', 'O', 'object'], ['K2', 'D', 'B', 'E', 'O', 'object'], ['K3', 'D', 'A', 'O', 'object'], ['K1', 'K2', 'K3']])
-------------
['Z']=merge([['K1', 'A', 'B', 'C', 'O', 'object'], ['K2', 'D', 'B', 'E', 'O', 'object'], ['K3', 'D', 'A', 'O', 'object'], ['K1', 'K2', 'K3']])
['Z', 'K1']=merge([['A', 'B', 'C', 'O', 'object'], ['K2', 'D', 'B', 'E', 'O', 'object'], ['K3', 'D', 'A', 'O', 'object'], ['K2', 'K3']])
['Z', 'K1', 'K2']=merge([['A', 'B', 'C', 'O', 'object'], ['D', 'B', 'E', 'O', 'object'], ['K3', 'D', 'A', 'O', 'object'], ['K3']])
['Z', 'K1', 'K2', 'K3']=merge([['A', 'B', 'C', 'O', 'object'], ['D', 'B', 'E', 'O', 'object'], ['D', 'A', 'O', 'object']])
['Z', 'K1', 'K2', 'K3', 'D']=merge([['A', 'B', 'C', 'O', 'object'], ['B', 'E', 'O', 'object'], ['A', 'O', 'object']])
['Z', 'K1', 'K2', 'K3', 'D', 'A']=merge([['B', 'C', 'O', 'object'], ['B', 'E', 'O', 'object'], ['O', 'object']])
['Z', 'K1', 'K2', 'K3', 'D', 'A', 'B']=merge([['C', 'O', 'object'], ['E', 'O', 'object'], ['O', 'object']])
['Z', 'K1', 'K2', 'K3', 'D', 'A', 'B', 'C']=merge([['O', 'object'], ['E', 'O', 'object'], ['O', 'object']])
['Z', 'K1', 'K2', 'K3', 'D', 'A', 'B', 'C', 'E']=merge([['O', 'object'], ['O', 'object'], ['O', 'object']])
['Z', 'K1', 'K2', 'K3', 'D', 'A', 'B', 'C', 'E', 'O']=merge([['object'], ['object'], ['object']])
[]

MRO['Z']=['Z', 'K1', 'K2', 'K3', 'D', 'A', 'B', 'C', 'E', 'O', 'object']
'''
class A(object): pass
class B(object): pass
class C(object): pass
class D(object): pass
class E(object): pass
class K1(A,B,C): pass
class K2(D,B,E): pass
class K3(D,A):   pass
class Z(K1,K2,K3): pass

print("=>".join([cls.__name__ for cls in Z.__mro__]))
'''
# Resulrt is
Z=>K1=>K2=>K3=>D=>A=>B=>C=>E=>object
'''

class A(object): pass
class B(object): pass
class C(object): pass
class D(object): pass
class E(object): pass
class K1(A,B,C): pass
class K2(B,D,E): pass
class K3(D,A):   pass
class Z(K1,K2,K3): pass
'''
# Result is
Traceback (most recent call last):
  File "mro_example.py", line 222, in <module>
    class Z(K1,K2,K3): pass
TypeError: Cannot create a consistent method resolution
order (MRO) for bases A, B, D

-------------
In this case merge will be as following
-------------
CPL[Z]=merge([['Z'], ['K1', 'A', 'B', 'C', 'O', 'object'], ['K2', 'B', 'D', 'E', 'O', 'object'], ['K3', 'D', 'A', 'O', 'object'], ['K1', 'K2', 'K3']])
-------------
['Z']=merge([['K1', 'A', 'B', 'C', 'O', 'object'], ['K2', 'B', 'D', 'E', 'O', 'object'], ['K3', 'D', 'A', 'O', 'object'], ['K1', 'K2', 'K3']])
['Z', 'K1']=([['A', 'B', 'C', 'O', 'object'], ['K2', 'B', 'D', 'E', 'O', 'object'], ['K3', 'D', 'A', 'O', 'object'], ['K2', 'K3']])
['Z', 'K1', 'K2']=merge([['A', 'B', 'C', 'O', 'object'], ['B', 'D', 'E', 'O', 'object'], ['K3', 'D', 'A', 'O', 'object'], ['K3']])
['Z', 'K1', 'K2', 'K3']=merge([['A', 'B', 'C', 'O', 'object'], ['B', 'D', 'E', 'O', 'object'], ['D', 'A', 'O', 'object']])
On this level error will be raised
'''
