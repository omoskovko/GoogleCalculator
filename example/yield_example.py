'''
  Following example demonstrate how SetUp and Teardown methods 
  are implemented in the pytest
'''

class MyHookimpl(object):
    def __init__(self):
        self.gen = None

    def __call__(self, func, *arc, **kwargs):
        self.gen = func(*arc, **kwargs)
        val = next(self.gen)
        return val

    def stop_gen(self):
        try:
          # Here TearDown will be invoked
          self.gen.send(None)
          raise Exception("has second yield")
        except StopIteration:
          pass

test_wrap = MyHookimpl()

@test_wrap
def my_test():
    print("SetUp")
    yield "my object is here"
    print("TearDown")
    

print(my_test)
print("Before teardown")

# Here TearDown will be invoked
test_wrap.stop_gen()

'''
# OutPut of this code will be as following

SetUp
my object is here
Before teardown
TearDown
'''