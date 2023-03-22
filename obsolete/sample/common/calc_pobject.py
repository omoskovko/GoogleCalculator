#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class CalcPObject(object):
    def __init__(self, driver):
        self.driver = driver
        self.NumStr = "0123456789."
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

    def click_clear(self):
        CElem = self.driver.find_element(*self.Btns["CE"])
        if not CElem.is_displayed():
            CElem = self.driver.find_element(*self.Btns["AC"])

        if not CElem.is_displayed():
            return False

        CElem.click()
        return self.driver.find_element_by_id("cwos").text == "0"

    def clear_result(self):
        wait = WebDriverWait(self, 30)
        wait.until(lambda driver: driver.click_clear())

    def open_calc(self, initText):
        wait = WebDriverWait(self.driver, 30)
        cElem = wait.until(lambda driver: driver.find_element_by_name("q"))

        cElem.send_keys(initText)
        cElem.send_keys(Keys.RETURN)

        cElem = wait.until(lambda driver: driver.find_element_by_id("cwos"))
        return cElem

    def calc_str(self, cStr):
        t = ""
        for c in cStr:
            t += c
            if t in self.NumStr:
                self.driver.find_element_by_xpath(
                    "//div[@role='button' and text()='%s']" % (t)
                ).click()
                t = ""

            if t in self.Btns:
                self.driver.find_element(*self.Btns[t]).click()
                t = ""

        time.sleep(2)
        return self.driver.find_element_by_id("cwos").text
