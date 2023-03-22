import pytest
from .common.project_data import CalcData


class TestCalc:
    @pytest.mark.parametrize(
        "test_id",
        [
            pytest.param("test_ln_calc", marks=pytest.mark.setup_func),
            "test_plus_calc",
            "test_multy_calc",
            pytest.param("test_long_calc", marks=pytest.mark.xfail),
        ],
    )
    def test_google_calc(self, test_loops, resource_handler, test_id):
        calc_str = CalcData.calcDict[test_id][0]
        check_res = CalcData.calcDict[test_id][1]

        ResVal = float(resource_handler.calc_str(calc_str))
        assert check_res == ResVal
