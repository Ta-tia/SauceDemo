from selenium.webdriver.common.by import By
from utils.wait import  Wait

class CheckoutYourInformation:
    #Locators:
    URL="https://www.saucedemo.com/cart.html"
    PAGE_TITLE=(By.CLASS_NAME, "title")

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIPCODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    CANCEL = (By.ID, "cancel")
    ERROR_BUTTON = (By.CLASS_NAME, "error-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver, timeout=10):
        self.driver=driver
        self.wait = Wait(driver)

    def open_page(self):
        """Open the webpage"""
        self.driver.get(self.URL)
        self.wait.for_element_visible(self.PAGE_TITLE)

    def get_page_title(self):
        """Get the page title text"""
        element = self.wait.for_element_visible(self.PAGE_TITLE)
        return element.text

    def is_page_loaded(self):
        """Verify that cart page is loaded"""
        try:
            element = self.wait.for_element_visible(self.PAGE_TITLE, timeout=5)
            return "checkout" in element.text.lower()
        except:
            return ""


    def enter_first_name(self, first_name):
        element = self.wait.for_element_visible(self.FIRST_NAME)
        element.clear()
        element.send_keys(first_name)

    def enter_last_name(self, last_name):
        element = self.wait.for_element_visible(self.LAST_NAME)
        element.clear()
        element.send_keys(last_name)

    def enter_zip_code(self, zip_code):
        element=self.wait.for_element_visible(self.ZIPCODE)
        element.clear()
        element.send_keys(zip_code)


    def click_continue_button(self):
        element=self.wait.for_element_clickable(self.CONTINUE)
        element.click()


    def fill_checkout_form(self, first_name, last_name, zip_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_zip_code(zip_code)

    def is_error_displayed(self):
        """Check if the error message is displayed when clicking on the 'Continue' button
        without filling out mandatory fields"""
        try:
            self.wait.for_element_visible(self.ERROR_MESSAGE, timeout=3)
            return True
        except:
            return False

    def get_error_message(self):
        """Get error message text if present"""
        try:
            element = self.wait.for_element_visible(self.ERROR_MESSAGE, timeout=3)
            return element.text.strip()
        except:
            return ""
