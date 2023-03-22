import math


class CalcData(object):
    calcDict = {
        "test_ln_calc": [
            "(ln(8)/ln(2))*(2+4)=",
            round((math.log(8) / math.log(2)) * (2 + 4), 10),
        ]
    }
    calcDict["test_plus_calc"] = ["742+3=", 742 + 3]
    calcDict["test_multy_calc"] = ["123*3.5=", 123 * 3.5]
    calcDict["test_long_calc"] = [
        "2*(3+4)-5*7/24-1=",
        round(2 * (3 + 4) - 5 * 7 / 24, 10),
    ]
