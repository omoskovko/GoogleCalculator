import os
import inspect
from selenium import webdriver
import unittest
#Project libs
from . import CalcPObject, CalcData

class PyGoogleCalc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
           cls.driver = webdriver.Firefox()
        except Exception:
           assertInfo = '''
                           Firefox is not installed and
                           system paramer "ChromDriver" is not defined.
                           Please add it with path to ChromDriver binary.
                           See https://sites.google.com/a/chromium.org/chromedriver/home
                           for more information or install Firefox.
                        '''
           assert 'ChromeDriver' in os.environ, assertInfo
           cls.driver = webdriver.Chrome(os.environ['ChromeDriver'])
        cls.driver.get('https://www.google.com')

        cls.cObj = CalcPObject(cls.driver)
        cls.cObj.open_calc('1+2')

    def setUp(self):
        self.tCaseName = self.id().split('.')[-1]
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
        mainFileName = inspect.stack()[0][1]
        outPngFile = os.path.abspath(os.path.join(os.path.dirname(mainFileName), 
                                     'output.png', self.tCaseName+'.png'))
        self.driver.get_screenshot_as_file(outPngFile)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
