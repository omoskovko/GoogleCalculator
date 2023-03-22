import os
import inspect
from selenium import webdriver
import unittest

# Project libs
from . import CalcPObject, CalcData


class PyGoogleCalc(unittest.TestCase):
    @staticmethod
    def get_out_path(*dirList):
        mainFileName = inspect.stack()[0][1]
        currOutFolder = "output.log"
        return os.path.abspath(
            os.path.join(os.path.dirname(mainFileName), currOutFolder, *dirList)
        )

    @classmethod
    def setUpClass(cls):
        try:
            cls.driver = webdriver.Firefox()
        except Exception:
            cls.driver = webdriver.Chrome()

        cls.driver.get("https://www.google.com")

        cls.cObj = CalcPObject(cls.driver)
        cls.cObj.open_calc("1+2")
        # cls.driver.set_window_size(945, 712)
        # cls.driver.set_window_position(400, 10)

    def setUp(self):
        self.tCaseName = self.id().split(".")[-1]
        self.cObj.clear_result()

    def test_ln_calc(self):
        calc_str = CalcData.calcDict[self.tCaseName][0]
        check_res = CalcData.calcDict[self.tCaseName][1]

        ResStr = float(self.cObj.calc_str(calc_str))
        self.assertEqual(check_res, ResStr)

    def test_plus_calc(self):
        calc_str = CalcData.calcDict[self.tCaseName][0]
        check_res = CalcData.calcDict[self.tCaseName][1]

        ResStr = float(self.cObj.calc_str(calc_str))
        self.assertEqual(check_res, ResStr)

    def test_multy_calc(self):
        calc_str = CalcData.calcDict[self.tCaseName][0]
        check_res = CalcData.calcDict[self.tCaseName][1]

        ResStr = float(self.cObj.calc_str(calc_str))
        self.assertEqual(check_res, ResStr)

    def test_long_calc(self):
        calc_str = CalcData.calcDict[self.tCaseName][0]
        check_res = CalcData.calcDict[self.tCaseName][1]

        ResStr = float(self.cObj.calc_str(calc_str))
        self.assertEqual(check_res, ResStr)

    def tearDown(self):
        outPngFile = self.get_out_path(self.tCaseName + ".png")
        self.driver.get_screenshot_as_file(outPngFile)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
