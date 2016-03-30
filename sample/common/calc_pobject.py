import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class CalcPObject(object):
    def __init__(self, driver):
        self.driver = driver
        self.NumStr = '0123456789.'
        self.BArray = ['=', '+', '-', '*', '/', '%', 'CE', '.', ')', '(', 'AC', 'ln(']
        self.Btns = {}
        self.Btns[self.BArray[0]]          = 'cwbt45'
        self.Btns[self.BArray[1]]          = 'cwbt46'
        self.Btns[self.BArray[2]]          = 'cwbt36'
        self.Btns[self.BArray[3]]          = 'cwbt26'
        self.Btns[self.BArray[4]]          = 'cwbt16'
        self.Btns[self.BArray[5]]          = 'cwbt05'
        self.Btns[self.BArray[6]]          = 'cwclrbtnCE'
        self.Btns[self.BArray[7]]          = 'cwbt44'
        self.Btns[self.BArray[8]]          = 'cwbt04'
        self.Btns[self.BArray[9]]          = 'cwbt03'
        self.Btns[self.BArray[10]]         = 'cwclrbtnAC'
        self.Btns[self.BArray[11]]         = 'cwbt12'

    def click_clear(self):
        CElem = self.driver.find_element_by_id(self.Btns['CE'])
        if not CElem.is_displayed():
           CElem = self.driver.find_element_by_id(self.Btns['AC'])

        if not CElem.is_displayed():
           return False

        CElem.click()
        return self.driver.find_element_by_id('cwos').text == '0'
            
    def clear_result(self):
        wait = WebDriverWait(self, 30)
        wait.until(lambda driver: driver.click_clear())

    def open_calc(self, initText):
        wait = WebDriverWait(self.driver, 30)
        cElem = wait.until(lambda driver: driver.find_element_by_name('q'))

        cElem.send_keys(initText)
        cElem.send_keys(Keys.RETURN)
        
        cElem = wait.until(lambda driver: driver.find_element_by_id('cwos'))
        return cElem

    def calc_str(self, cStr):
        t = ''
        for c in cStr:
           t = t + c
           if t in self.NumStr:
              self.driver.find_element_by_xpath("//span[text()='%s']" % (t)).click()
              t = ''

           if t in self.BArray:
              self.driver.find_element_by_id(self.Btns[t]).click()
              t = ''

        time.sleep(2)
        return self.driver.find_element_by_id('cwos').text
