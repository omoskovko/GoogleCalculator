'''
https://www.python.org/dev/peps/pep-0484/
PEP:	484
Title:	Type Hints
Author:	Guido van Rossum <guido at python.org>, Jukka Lehtosalo <jukka.lehtosalo at iki.fi>, ?ukasz Langa <lukasz at python.org>
BDFL-Delegate:	Mark Shannon
Discussions-To:	Python-Dev <python-dev at python.org>
Status:	Provisional
Type:	Standards Track
Created:	29-Sep-2014
Python-Version:	3.5
Post-History:	16-Jan-2015,20-Mar-2015,17-Apr-2015,20-May-2015,22-May-2015
Resolution:	https://mail.python.org/pipermail/python-dev/2015-May/140104.html
'''

'''
http://mypy-lang.org/

Python syntax

Mypy type checks programs that have type annotations conforming to PEP 484. 
Getting started is easy if you know Python. The aim is to support almost all Python language constructs in mypy. 

pip install mypy
mypy program.py
'''
from typing import TypeVar, Generic

MyInt = TypeVar('MyInt')
S = TypeVar('S')

class MyClass(Generic[MyInt, S]):
    def meth_1(self, x: MyInt) -> MyInt:  # T here
        return x
    def meth_2(self, x: S) -> S:  # and here are always the same
        return x

a = MyClass()  # type: MyClass[int, str]
a.meth_1(1)    # OK
a.meth_2("a")  # This is an error!
