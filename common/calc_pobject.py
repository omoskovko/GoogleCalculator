#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from .page import BasePage


class CalcPObject(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

        self.Btns = {}
        self.Btns["="] = (By.XPATH, "//div[@role='button' and text()='=']")
        self.Btns["+"] = (By.XPATH, "//div[@role='button' and text()='+']")
        self.Btns["/"] = (By.XPATH, "//div[@role='button' and text()='÷']")
        self.Btns["*"] = (By.XPATH, "//div[@role='button' and text()='×']")
        self.Btns["-"] = (By.XPATH, "//div[@role='button' and text()='−']")
        self.Btns["%"] = (By.XPATH, "//div[@role='button' and text()='%']")
        self.Btns["."] = (By.XPATH, "//div[@role='button' and text()='.']")
        self.Btns[")"] = (By.XPATH, "//div[@role='button' and text()=')']")
        self.Btns["("] = (By.XPATH, "//div[@role='button' and text()='(']")
        self.Btns["CE"] = (By.XPATH, "//div[@role='button' and text()='CE']")
        self.Btns["AC"] = (By.XPATH, "//div[@role='button' and text()='AC']")
        self.Btns["ln("] = (By.XPATH, "//div[@role='button' and contains(text(),'ln')]")

        for t in range(10):
            self.Btns[str(t)] = (
                By.XPATH,
                "//div[@role='button' and text()='%s']" % (t),
            )

    def click_clear(self):
        CElem = self.wait_until(*self.Btns["CE"])
        if not CElem.is_displayed():
            CElem = self.wait_until(*self.Btns["AC"])

        if not CElem.is_displayed():
            return False

        CElem.click()
        return self._driver.find_element(By.ID, "cwos").text == "0"

    def clear_result(self):
        wait = WebDriverWait(self, 30)
        wait.until(lambda driver: driver.click_clear())

    def calc_str(self, cStr):
        self.clear_result()

        t = ""
        for c in cStr:
            t += c
            if t in self.Btns:
                self.wait_until(*self.Btns[t]).click()
                t = ""

        time.sleep(2)
        return self._driver.find_element(By.ID, "cwos").text
