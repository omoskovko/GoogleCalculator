'''
  Following example demonstrate how SetUp and Teardown methods 
  are implemented in the pytest
'''

gen = None

def test_wrap(func, *arc, **kwargs):
    global gen 
    gen = func(*arc, **kwargs)
    val = next(gen)
    return val

@test_wrap
def my_test():
    print("SetUp")
    yield "my_func str"
    print("TearDown")
    

print(my_test)
print("Before teardown")

try:
  gen.send(None)
except StopIteration:
  pass

'''
# OutPut of this code will be as following

SetUp
my_func str
Before teardown
TearDown
'''