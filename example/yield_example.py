class MyHookimpl(object):
    def __init__(self, hook_name):
        self.gen = None
        self.hook_name = hook_name

    def __call__(self, func):
        print("Hook is invoked")
        self.gen = func(self.hook_name)
        val = next(self.gen)
        return val

    def stop_gen(self):
        try:
          # Here TearDown will be invoked
          self.gen.send(None)
          raise Exception("has second yield")
        except StopIteration:
          pass

test_wrap = MyHookimpl("Yield example")

@test_wrap
def my_test(test_name):
    print("SetUp {0}".format(test_name))
    yield "my object is here"
    print("TearDown {0}".format(test_name))
    

print(my_test)

print("Next step")
aaa = my_test

print("aaa={0}".format(aaa))
print("Before teardown")

# Here TearDown will be invoked
test_wrap.stop_gen()

'''
# OutPut of this code will be as following

Hook is invoked
SetUp Yield example
my object is here
Next step
aaa=my object is here
Before teardown
TearDown Yield example
'''