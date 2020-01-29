from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

from .calc_pobject import CalcPObject
from .page_loader import require_loaded
from .page import BasePage


class GoogleOneBox(BasePage):
    """This class models a page that has a google search bar."""

    def __init__(self, driver, url):
        BasePage.__init__(self, driver)

        #self._driver = driver
        self._url = url

    def is_loaded(self):
        try:
            self._driver.find_element_by_name("q")
            return True
        except NoSuchElementException:
            return False

    def load(self):
        self._driver.get(self._url)
        self.wait_until(By.NAME, "q")

    @require_loaded
    def search_for(self, search_term):
        element = self._driver.find_element_by_name("q")
        element.send_keys(search_term)
        element.submit()
        return CalcPObject(self._driver)
