'''
https://www.python.org/dev/peps/pep-0342/
'''

import inspect
from collections import OrderedDict

class MyHookimpl(object):
    def __init__(self):
        self.func_regs = OrderedDict()

    def __call__(self, hookfunc):
        def hook_func(*arc, **kwargs):
            if not hookfunc.__name__ in self.func_regs:
                if not inspect.isgeneratorfunction(hookfunc):
                   raise Exception("{0} has no yield".format(hookfunc.__name__))

                gen = hookfunc(*arc, **kwargs)
                val = next(gen)
                self.__dict__[hookfunc.__name__] = val #(val, gen)
                self.func_regs[hookfunc.__name__] = (gen, hook_func)

            return self.__dict__[hookfunc.__name__]

        self.__dict__[hookfunc.__name__] = hook_func
        return hook_func

    def stop_gen(self, gen_name=None):
          # Here TearDown will be invoked
          err = None
          gen_dict = OrderedDict()

          if gen_name:
              gen, func = self.func_regs.pop(gen_name)
              gen_dict[gen_name] = (gen, func)
          else:
              gen_dict = self.func_regs

          reg_dict_len = len(gen_dict)
          for i in range(reg_dict_len):
              fname, (gen, func) = gen_dict.popitem()

          #for val, g in reversed(self.func_regs.values()):
              try:
                  gen.send(None)
                  err = Exception("{0} has second yield".format(fname))
              except StopIteration:
                  del self.__dict__[fname]
                  self.__dict__[fname] = func
          if err:
             raise err

test_wrap = MyHookimpl()

print("-- Def --")
@test_wrap
def test_name():
    print("---------------------")
    print("SetUp test_name")
    yield "Basic value"
    print("TearDown test_name")
    print("---------------------")
    
@test_wrap
def my_test(param1):
    print("---------------------")
    print("SetUp my_test")
    val = "My test value is: " + param1
    yield val
    print("TearDown my_test")
    print("---------------------")
    
@test_wrap
def my_next_test(param1, param2):
    print("---------------------")
    print("SetUp my_next_test")
    val = param1 + " - " + param2
    yield val
    print("TearDown my_next_test")
    print("---------------------")

print("-- End Def --")
print("- step 1 --------------")
t = test_wrap.my_test("Test global")
print("t={0}".format(t))
print(test_wrap.test_name())

print("- step 2 --------------")
t = my_test("aaaaaaaaaa")
print("t={0}".format(t))
#print(dir(test_wrap.test_name))

test_wrap.stop_gen()

print("- step 3 --------------")
#print(test_wrap.test_name())
print(test_wrap.my_test(test_wrap.test_name()))
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
