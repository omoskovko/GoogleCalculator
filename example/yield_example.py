"""
https://www.python.org/dev/peps/pep-0342/
"""

import inspect
from collections import OrderedDict


class MyHookimpl(object):
    def __init__(self):
        self.func_regs = OrderedDict()

    def __call__(self, hookfunc):
        if not hookfunc.__name__ in self.func_regs:
            if not inspect.isgeneratorfunction(hookfunc):
                raise Exception("{0} has no yield".format(hookfunc.__name__))

            self.__dict__[hookfunc.__name__] = None  # (val, gen)
            self.func_regs[hookfunc.__name__] = (hookfunc, None)
        return hookfunc

    def init_gen(self, gen_name):
        if not gen_name.__name__ in self.func_regs:
            raise Exception("{0} is not found".format(gen_name.__name__))

        if self.__dict__[gen_name.__name__] is not None:
            _, gen = self.func_regs[gen_name.__name__]
            val = self.__dict__[gen_name.__name__]
            return val, gen

        args = gen_name.__code__.co_varnames[: gen_name.__code__.co_argcount]
        res = {v: self.__dict__[v] for v in self.__dict__ if v in args}

        for f_name in [v for v in res if res[v] is None]:
            val, gen = self.init_gen(self.func_regs[f_name][0])
            self.__dict__[f_name] = val
            res[f_name] = val

        gen = gen_name(**res)
        val = next(gen)
        self.__dict__[gen_name.__name__] = val
        self.func_regs[gen_name.__name__] = (gen_name, gen)
        return val, gen

    def run_gen(self, gname=None):
        if gname is None:
            for gen_name in self.func_regs:
                self.init_gen(self.func_regs[gen_name][0])
        else:
            self.init_gen(gname)

    def stop_gen(self, gen_name=None):
        # Here TearDown will be invoked
        err = None
        gen_dict = OrderedDict()

        if gen_name:
            func, gen = self.func_regs.pop(gen_name)
            gen_dict[gen_name] = (func, gen)
        else:
            gen_dict = self.func_regs

        reg_dict_len = len(gen_dict)
        for i in range(reg_dict_len):
            fname, (func, gen) = gen_dict.popitem()

            # for val, g in reversed(self.func_regs.values()):
            try:
                gen.send(None)
                err = Exception("{0} has second yield".format(fname))
            except StopIteration:
                del self.__dict__[fname]
                self.__dict__[fname] = func
        if err:
            raise err


test_wrap = MyHookimpl()


@test_wrap
def test_name():
    print("---------------------")
    print("SetUp test_name")
    yield "Basic value"
    print("TearDown test_name")
    print("---------------------")


@test_wrap
def my_test(test_name):
    print("---------------------")
    print("SetUp my_test")
    val = f"My test value is: {test_name}"
    yield val
    print("TearDown my_test")
    print("---------------------")


@test_wrap
def my_next_test(my_test, test_name):
    print("---------------------")
    print("SetUp my_next_test")
    val = test_name + " - " + my_test
    yield val
    print("TearDown my_next_test")
    print("---------------------")


test_wrap.run_gen()
test_wrap.stop_gen()

'''
 @contextlib.contextmanager

    This function is a decorator that can be used to define a factory function for with statement context managers, 
    without needing to create a class or separate __enter__() and __exit__() methods.

    While many objects natively support use in with statements, sometimes a resource needs to be managed 
    that isn't a context manager in its own right, and doesn't implement a close() method for use with contextlib.closing

    The function being decorated must return a generator-iterator when called. 
    This iterator must yield exactly one value, which will be bound to the targets in the with statement's as clause, if any.
'''

import contextlib

@contextlib.contextmanager
def transaction():
    print('begin')
    try:
        yield from do_it()
    except:
        print('rollback')
        raise
    else:
        print('commit')

def do_it():
    print('Refactored initial setup')
    yield # Body of with-statement is executed here
    print('Refactored finalization of successful transaction')

def gene():
    for i in range(2):
        with transaction():
            yield i

for i in gene():
    print('main: i =', i)
