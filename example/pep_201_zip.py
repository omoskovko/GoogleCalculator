"""
https://www.python.org/dev/peps/pep-0201/
PEP:	201
Title:	Lockstep Iteration
Author:	barry at python.org (Barry Warsaw)
Status:	Final
Type:	Standards Track
Created:	13-Jul-2000
Python-Version:	2.0
Post-History:	27-Jul-2000
"""

# Here are some examples, based on the reference implementation below:
a = (1, 2, 3, 4)
b = (5, 6, 7, 8)
c = (9, 10, 11)
d = (12, 13)

print(list(zip(a, b)))
# [(1, 5), (2, 6), (3, 7), (4, 8)]

print(list(zip(a, d)))
# [(1, 12), (2, 13)]

print(list(zip(a, b, c, d)))
# [(1, 5, 9, 12), (2, 6, 10, 13)]

# Note that when the sequences are of the same length, zip() is reversible:
a = (1, 2, 3)
b = (4, 5, 6)
x = list(zip(a, b))
y = list(zip(*x))  # alternatively, apply(zip, x)
z = list(zip(*y))  # alternatively, apply(zip, y)
print(list(x))
# [(1, 4), (2, 5), (3, 6)]
print(list(y))
# [(1, 2, 3), (4, 5, 6)]
print(list(z))
# [(1, 4), (2, 5), (3, 6)]
print(x == z)
# True

"""

Reference Implementation

Here is a reference implementation, in Python of the zip() built-in function. 
This will be replaced with a C implementation after final approval:

def zip(*args):
    if not args:
        raise TypeError('zip() expects one or more sequence arguments')
    ret = []
    i = 0
    try:
        while 1:
            item = []
            for s in args:
                item.append(s[i])
            ret.append(tuple(item))
            i = i + 1
    except IndexError:
        return ret

"""
