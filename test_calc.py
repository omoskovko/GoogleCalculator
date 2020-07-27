import pytest
from common.project_data import CalcData
from conftest import option

@pytest.fixture(params=[v for v in range(int(option.testLoops))])
def test_loops(request):
    return request.param

class TestCalc:
    @pytest.fixture(autouse=True)
    def process_func(self, request, resource_handler):
        '''
          The class-level process_func fixture is marked with autouse=true which implies 
          that all test methods in the class will use this fixture without a need to state it 
          in the test function signature or with a class-level usefixtures decorator.
          http://doc.pytest.org/en/latest/fixture.html#autouse-fixtures-xunit-setup-on-steroids
        '''
        print("SetUp function {0}".format(request.function.__name__))
        print(request.keywords.node.funcargs.keys())
        resource_handler.clear_result()

        yield

        print("TearDown function {0}".format(request.function.__name__))
        print(request.keywords.node.funcargs.keys())
        resource_handler.clear_result()
        

    @pytest.mark.parametrize("test_id", 
        ["test_ln_calc", "test_plus_calc", "test_multy_calc", pytest.param("test_long_calc", marks=pytest.mark.xfail)]
    )
    def test_google_calc(self, test_loops, resource_handler, test_id):
        calc_str = CalcData.calcDict[test_id][0]
        check_res = CalcData.calcDict[test_id][1]

        ResVal = float(resource_handler.calc_str(calc_str))
        assert check_res == ResVal

