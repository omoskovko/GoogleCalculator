from inspect import signature
from collections import OrderedDict

class MyHookimpl(object):
    def __init__(self):
        self.func_regs = OrderedDict()

    def __call__(self, func):
        parameters = signature(func).parameters
        params_list = []
        for p in parameters:
            if p in self.func_regs:
               params_list.append(self.func_regs[p][0])

        gen = (func(*params_list))
        val = next(gen)
        self.func_regs[func.__name__] = (val, gen)
        return val

    def stop_gen(self):
          # Here TearDown will be invoked
          err = None
          for val, g in self.func_regs.values():
              try:
                  g.send(None)
                  err = Exception("{0} has second yield".format(val))
              except StopIteration:
                pass
          if err:
             raise err

test_wrap = MyHookimpl()

@test_wrap
def test_name():
    print("SetUp Basic values")
    yield "Basic value"
    print("TearDown Basic values")
    
@test_wrap
def my_test(test_name):
    print("SetUp my_test")
    val = "My test value is: " + test_name
    yield val
    print("TearDown my_test")
    
@test_wrap
def my_next_test(test_name, my_test):
    print("SetUp my_next_test")
    val = test_name + " - " + my_test
    yield val
    print("TearDown my_next_test")
    

print(my_next_test)

print("- Next step -----------")
aaa = my_test

print("aaa={0}".format(aaa))
print("- Before teardown -----")

# Here TearDown will be invoked
test_wrap.stop_gen()

'''
# OutPut of this code will be as following

SetUp Basic values
SetUp my_test
SetUp my_next_test
Basic value - My test value is: Basic value
- Next step -----------
aaa=My test value is: Basic value
- Before teardown -----
TearDown Basic values
TearDown my_test
TearDown my_next_test
'''