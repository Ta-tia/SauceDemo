"""Explicit wait utilities for reliable test execution"""

from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Wait:
    def __init__(self, driver, default_timeout=10):
        self.driver=driver
        self.timeout=default_timeout


    def for_element_visible(self, locator, timeout=None):
        """Wait for the element to be visible"""
        wait_time = timeout or self.timeout
        return WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(locator))

    def for_element_clickable(self, locator, timeout=None):
        """Wait for the element to be clickable"""
        wait_time=timeout or self.timeout
        return WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located(locator))

    def for_element_present(self, locator, timeout=None):
        """Wait for the element to be present in DOM"""
        wait_time=timeout or self.timeout
        return WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located(locator))


    def for_elements_present(self, locator, timeout=None):
        """Wait for the elements to be present in DOM"""
        wait_time=timeout or self.timeout
        return WebDriverWait(self.driver, wait_time).until(EC.presence_of_all_elements_located(locator))

    def for_text_in_element(self, locator, text, timeout=None):
        """Wait for the specific text to appear in the element"""
        wait_time=timeout or self.timeout
        return WebDriverWait(self.driver, wait_time).until(EC.text_to_be_present_in_element(locator, text))

    def for_url_contains(self, text, timeout=None):
        """Wait for the URL to contain specific text"""
        wait_time=timeout or self.timeout
        return WebDriverWait(self.driver, wait_time).until(EC.url_contains(text))
