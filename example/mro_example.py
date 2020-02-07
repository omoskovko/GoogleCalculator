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

In this case the inheritance graph can be drawn as

                              6
                             ---
    Level 3                 | O |                  (more general)
                          /  ---  \
                         /    |    \                      |
                        /     |     \                     |
                       /      |      \                    |
                      ---    ---    ---                   |
    Level 2        3 | D | 4| E |  | F | 5                |
                      ---    ---    ---                   |
                       \  \ _ /       |                   |
                        \    / \ _    |                   |
                         \  /      \  |                   |
                          ---      ---                    |
    Level 1            1 | B |    | C | 2                 |
                          ---      ---                    |
                            \      /                      |
                             \    /                      \ /
                               ---
    Level 0                 0 | A |                (more specialized)
                               ---


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

                               6
                              ---
    Level 3                  | O |
                           /  ---  \
                          /    |    \
                         /     |     \
                        /      |      \
                      ---     ---    ---
    Level 2        2 | E | 4 | D |  | F | 5
                      ---     ---    ---
                       \      / \     /
                        \    /   \   /
                         \  /     \ /
                          ---     ---
    Level 1            1 | B |   | C | 3
                          ---     ---
                           \       /
                            \     /
                              ---
    Level 0                0 | A |
                              ---

Notice that the class E, which is in the second level of the hierarchy, precedes the class C, 
which is in the first level of the hierarchy, i.e. E is more specialized than C, even if it is in a higher level.

A lazy programmer can obtain the MRO directly from Python 2.2, since in this case it coincides with the Python 2.3 linearization. 
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


                                       6
                                      ---
    Level 3                   ------ | O |-------
                             /        ---        \
                            /       /  |  \       \
                           /       /   |   \       \
                          /       /    |    \       \
                         /       /     |     \       \
                        /       /      |      \       \
                      ---     ---     ---     ---    ---   
    Level 2        5 | A | 6 | B | 7 | C | 4 | D | 8| E | 
                      ---     ---     ---     ---    ---   
                       \  \____\_     /        /\      /
                        \      |\ \__/__      /  \    /
                         \     | \  /   \    /    \  /
                          \    |  \/     \__/__    \/
                           |   |  /\       /   \   /\
                           |   | /  \     /     \_/  \
                           |   |/    \   /       /\   \
                          -------      -------      ----
    Level 1            1 |   K1  |  2 |   K2  | 3  | K3 | 
                          -------      -------      ----
                              \           |      /
                               \          |     /
                                   ------------
    Level 0                     0 |      Z     |
                                   ------------
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
