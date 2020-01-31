from inspect import signature
from collections import OrderedDict

class MyHookimpl(object):
    def __init__(self, ses):
        self.func_regs = OrderedDict()
        self.session = ses

    def __call__(self, func):
        def hook_func(*arc, **kwargw):
            if self.session == "function" and func.__name__ in self.func_regs:
               self.stop_gen(func.__name__)

            if not func.__name__ in self.func_regs:
                #print("Execute {0}".format(func.__name__))
                gen = func(*arc, **kwargw)
                val = next(gen)
                self.func_regs[func.__name__] = (val, gen)
            else:
                val = self.func_regs[func.__name__][0]
            return val
        return hook_func

    def stop_gen(self, gen_name=None):
          # Here TearDown will be invoked
          err = None
          gen_dict = OrderedDict()

          if gen_name:
              val, gen = self.func_regs.pop(gen_name)
              gen_dict[gen_name] = (val, gen)
          else:
              gen_dict = self.func_regs

          reg_dict_len = len(gen_dict)
          for i in range(reg_dict_len):
              fname, val = gen_dict.popitem()

          #for val, g in reversed(self.func_regs.values()):
              try:
                  val[1].send(None)
                  err = Exception("{0} has second yield".format(fname))
              except StopIteration:
                pass
          if err:
             raise err

test_wrap = MyHookimpl("session")

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
    val = "My test value is: " + test_name
    yield val
    print("TearDown my_test")
    print("---------------------")
    
@test_wrap
def my_next_test(test_name, my_test):
    print("---------------------")
    print("SetUp my_next_test")
    val = test_name + " - " + my_test
    yield val
    print("TearDown my_next_test")
    print("---------------------")

print("- step 1 --------------")
print(my_test(test_name()))

print("- step 2 --------------")
print(my_next_test(test_name(), my_test(test_name())))

test_wrap.stop_gen()
