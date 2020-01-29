import pytest
#from simple_salesforce import Salesforce
from .common.project_data import CalcData

class TestCalc:
    @pytest.mark.parametrize("test_id", ["test_ln_calc", "test_plus_calc", "test_multy_calc", "test_long_calc"])
    def test_google_calc(self, resource_handler, test_id):
        calc_str = CalcData.calcDict[test_id][0]
        check_res = CalcData.calcDict[test_id][1]

        ResVal = float(resource_handler.calc_str(calc_str))
        assert check_res == ResVal

