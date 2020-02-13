https://www.python.org/dev/peps/pep-0328/
`
PEP:	328
Title:	Imports: Multi-Line and Absolute/Relative
Author:	Aahz <aahz at pythoncraft.com>
Status:	Final
Type:	Standards Track
Created:	21-Dec-2003
Python-Version:	2.4, 2,5, 2.6
Post-History:	8-Mar-2004
`


#Guido's Decision

Guido has Pronounced [1] that relative imports will use leading dots. 
A single leading dot indicates a relative import, starting with the current package. 
Two or more leading dots give a relative import to the parent(s) of the current package, 
one level per dot after the first. Here's a sample package layout:
`
package/
    __init__.py
    subpackage1/
        __init__.py
        moduleX.py
        moduleY.py
    subpackage2/
        __init__.py
        moduleZ.py
    moduleA.py
`
Assuming that the current file is either moduleX.py or subpackage1/__init__.py, following are correct usages of the new syntax:
`
from .moduleY import spam
from .moduleY import spam as ham
from . import moduleY
from ..subpackage1 import moduleY
from ..subpackage2.moduleZ import eggs
from ..moduleA import foo
from ...package import bar
from ...sys import path
`
Note that while that last case is legal, it is certainly discouraged ("insane" was the word Guido used).

Relative imports must always use from <> import; import <> is always absolute. 
Of course, absolute imports can use from <> import by omitting the leading dots. 
The reason import .foo is prohibited is because after
`
import XXX.YYY.ZZZ
`
then
`
XXX.YYY.ZZZ
`
is usable in an expression. But
`
.moduleY
`
is not usable in an expression.
