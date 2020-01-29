import pytest
from .common.project_data import CalcData

class TestCalc:
    @pytest.fixture(autouse=True)
    def process_func(self, request, resource_handler):
        print("SetUp function {0}".format(request.function.__name__))
        resource_handler.clear_result()

        yield

        print("TearDown function {0}".format(request.function.__name__))
        resource_handler.clear_result()
        

    @pytest.mark.parametrize("test_id", 
        ["test_ln_calc", "test_plus_calc", "test_multy_calc", pytest.param("test_long_calc", marks=pytest.mark.xfail)]
    )
    def test_google_calc(self, resource_handler, test_id):
        calc_str = CalcData.calcDict[test_id][0]
        check_res = CalcData.calcDict[test_id][1]

        ResVal = float(resource_handler.calc_str(calc_str))
        assert check_res == ResVal

