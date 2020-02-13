'''
https://www.python.org/dev/peps/pep-0487/
PEP:	487
Title:	Simpler customisation of class creation
Author:	Martin Teichmann <lkb.teichmann at gmail.com>,
Status:	Final
Type:	Standards Track
Created:	27-Feb-2015
Python-Version:	3.6
Post-History:	27-Feb-2015, 5-Feb-2016, 24-Jun-2016, 2-Jul-2016, 13-Jul-2016
Replaces:	422
Resolution:	https://mail.python.org/pipermail/python-dev/2016-July/145629.html


Proposal

While there are many possible ways to use a metaclass, the vast majority of use cases falls into just three categories: 
some initialization code running after class creation, 
the initialization of descriptors and keeping the order in which class attributes were defined.

The first two categories can easily be achieved by having simple hooks into the class creation:

    An __init_subclass__ hook that initializes all subclasses of a given class.
    upon class creation, a __set_name__ hook is called on all the attribute (descriptors) defined in the class, and

The third category is the topic of another PEP, PEP 520.

As an example, the first use case looks as follows:
'''

class QuestBase:
   swallow= []
   # this is implicitly a @classmethod (see below for motivation)
   def __init_subclass__(cls, swallow, **kwargs):
       super().__init_subclass__(**kwargs)
       cls.swallow.append(swallow)

class Quest(QuestBase, swallow="african"):
   pass

class Amr(QuestBase, swallow="amr"):
   pass

print(QuestBase.swallow)


class Repository():
    _registry = {}

    def __init_subclass__(cls, scm_type=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if scm_type is not None:
            cls._registry[scm_type] = cls

    @classmethod
    def __class_getitem__(cls, base):
        if not base:
            # makes normal use of class possible
            return cls
        else:
            # construct a new type using the given base class and also remember the attribute for future instantiations
            return cls._registry[base]

class MainHgRepository(Repository, scm_type="main"):
    pass

main = Repository['main']()
print(type(main))

class GenericGitRepository(Repository, scm_type="GIT"):
    pass

rep = Repository()

print(Repository._registry)

main = Repository['GIT']()
print(type(main))
