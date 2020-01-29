import pytest
#from simple_salesforce import Salesforce
from .common.project_data import CalcData

class TestCalc:
    def test_ln_calc(self, resource_handler):
        tCaseName = "test_ln_calc"
        calc_str = CalcData.calcDict[tCaseName][0]
        check_res = CalcData.calcDict[tCaseName][1]

        ResVal = float(resource_handler.calc_str(calc_str))
        assert check_res == ResVal

    def test_plus_calc(self, resource_handler):
        tCaseName = "test_plus_calc"
        calc_str = CalcData.calcDict[tCaseName][0]
        check_res = CalcData.calcDict[tCaseName][1]

        ResVal = float(resource_handler.calc_str(calc_str))
        assert check_res == ResVal

    def test_multy_calc(self, resource_handler):
        tCaseName = "test_multy_calc"
        calc_str = CalcData.calcDict[tCaseName][0]
        check_res = CalcData.calcDict[tCaseName][1]

        ResVal = float(resource_handler.calc_str(calc_str))
        assert check_res == ResVal

    def test_long_calc(self, resource_handler):
        tCaseName = "test_long_calc"
        calc_str = CalcData.calcDict[tCaseName][0]
        check_res = CalcData.calcDict[tCaseName][1]

        ResVal = float(resource_handler.calc_str(calc_str))
        assert check_res == ResVal
