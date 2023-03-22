from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.errorhandler import (
    InvalidElementStateException,
    NoSuchElementException,
)


class BasePage(object):
    """
    Page object Class with basic methods
    """

    def __init__(self, driver):
        self._driver = driver

    def wait_until(self, by, value, timeout=90, vDrv=None):
        """
        Wait for element is found and return it
        """
        wDriver = vDrv
        if not wDriver:
            wDriver = self._driver

        vMessage = "Element By='{0}', Value={1} is not found".format(by, value)
        return WebDriverWait(
            wDriver,
            timeout,
            ignored_exceptions=(
                InvalidElementStateException,
                NoSuchElementException,
            ),
        ).until(lambda driver: driver.find_element(by, value), vMessage)

    def wait_until_elems(self, by, value, timeout=90, vDrv=None):
        """
        Wait for element is found and return it
        """
        wDriver = vDrv
        if not wDriver:
            wDriver = self._driver

        vMessage = "Element By='{0}', Value={1} is not found".format(by, value)
        return WebDriverWait(
            wDriver,
            timeout,
            ignored_exceptions=(
                InvalidElementStateException,
                NoSuchElementException,
            ),
        ).until(lambda driver: driver.find_elements(by, value), vMessage)

    def wait_until_not(self, by, value, timeout=90, vDrv=None):
        """
        Wait for element is disappeared
        """
        wDriver = vDrv
        if not wDriver:
            wDriver = self._driver

        vMessage = "Element By='{0}', Value={1} is still present".format(by, value)
        WebDriverWait(
            wDriver,
            timeout,
            ignored_exceptions=(
                InvalidElementStateException,
                NoSuchElementException,
            ),
        ).until_not(
            lambda driver: driver.find_element(by, value).is_displayed(), vMessage
        )

    def wait_for_text_in_element(self, text_value, by, value, timeout=90, vDrv=None):
        """
        Wait for element is found and return it
        """
        wDriver = vDrv
        if not wDriver:
            wDriver = self._driver

        vMessage = "Element By='{0}', Value={1}: text '{2}' is not found".format(
            by, value, text_value
        )
        return WebDriverWait(
            wDriver,
            timeout,
            ignored_exceptions=(
                InvalidElementStateException,
                NoSuchElementException,
            ),
        ).until(
            lambda driver, t_str=text_value: t_str
            in driver.find_element(by, value).text,
            vMessage,
        )

    def wait_clear(self, by, value, timeout=90, vDrv=None):
        """
        Should be used for input fields
        Wait while element is found and can be cleared.
        If InvalidElementStateException is raised than ignore it.
        """
        wDriver = vDrv
        if not wDriver:
            wDriver = self._driver

        def clear_field(driver, vBy=by, sValue=value):
            iElem = driver.find_element(vBy, sValue)
            iElem.clear()
            return iElem

        vMessage = "Element By='{0}', Value={1} is not currently interactable and may not be manipulated".format(
            by, value
        )
        return WebDriverWait(
            driver=wDriver,
            timeout=timeout,
            ignored_exceptions=(
                InvalidElementStateException,
                NoSuchElementException,
            ),
        ).until(clear_field, vMessage)

    def get_text_from_field(self, by, locator, isClosed=False):
        retText = "Closed"
        if isClosed:
            self.wait_until_not(by, locator)
        else:
            fh = self.wait_until(by, locator)
            retText = fh.text

        return retText

    def set_input_field(self, by, locator, sValue, timeout=90, vDrv=None):
        """
        Wait while element is found and can be clicked.
        If InvalidElementStateException is raised than ignore it.
        """
        wDriver = vDrv
        if not wDriver:
            wDriver = self._driver

        def set_text_val(driver, sVal=sValue, vBy=by, sLc=locator):
            iElem = driver.find_element(vBy, sLc)
            iElem.clear()
            iElem.send_keys(sVal)
            return True

        vMessage = "Element By='{0}', Value={1} is not currently interactable and may not be manipulated".format(
            by, locator
        )
        return WebDriverWait(
            driver=wDriver,
            timeout=timeout,
            ignored_exceptions=(
                InvalidElementStateException,
                NoSuchElementException,
            ),
        ).until(set_text_val, vMessage)

    def click_on_field(self, by, locator, timeout=90, vDrv=None):
        """
        Wait while element is found and can be clicked.
        If InvalidElementStateException is raised than ignore it.
        """
        wDriver = vDrv
        if not wDriver:
            wDriver = self._driver

        def click_field(driver, vBy=by, sValue=locator):
            iElem = driver.find_element(vBy, sValue)
            iElem.click()
            return True

        vMessage = "Element By='{0}', Value={1} is not currently interactable and may not be manipulated".format(
            by, locator
        )
        return WebDriverWait(
            driver=wDriver,
            timeout=timeout,
            ignored_exceptions=(
                InvalidElementStateException,
                NoSuchElementException,
            ),
        ).until(click_field, vMessage)

    def get_field_property(self, by, locator, pName):
        iField = self.wait_until(by, locator)
        return iField.get_property(pName)

    def get_field_attribute(self, by, locator, pName):
        iField = self.wait_until(by, locator)
        return iField.get_attribute(pName)

    def get_list_of_option_text(self, by, locator):
        sObject = Select(self.wait_until(by, locator))
        return [o.text for o in sObject.options]

    def get_selected_option(self, by, locator):
        sObject = Select(self.wait_until(by, locator))
        return sObject.first_selected_option.text

    def select_option_by_value(self, by, locator, value):
        sObject = Select(self.wait_until(by, locator))
        sObject.select_by_value(value)
        return sObject.first_selected_option.text

    def select_option_by_visible_text(self, by, locator, value):
        sObject = Select(self.wait_until(by, locator))
        sObject.select_by_visible_text(value)
        return sObject.first_selected_option.text

    def get_current_url(self):
        return self._driver.current_url

    def is_displayed(self, by, locator):
        return self.wait_until(by, locator).is_displayed()
