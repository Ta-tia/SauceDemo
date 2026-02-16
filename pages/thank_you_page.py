from selenium.webdriver.common.by import By
from utils.wait import  Wait

class CheckoutComplete():
    #Locators
    TITLE = (By.CLASS_NAME, "title")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")
    CONFIRMATION_IMAGE = (By.CLASS_NAME, "pony_express")


    def __init__(self, driver, timeout=10):
        self.driver=driver
        self.wait=Wait(driver)

    def get_page_title(self):
        """Get the page title text"""
        element = self.wait.for_element_visible(self.TITLE)
        return element.text

    def get_confirmation_message(self):
        """Get the confirmation message text"""
        element = self.wait.for_element_visible(self.COMPLETE_HEADER)
        return element.text

    def get_confirmation_image(self):
        """Get the confirmation message image"""
        element = self.wait.for_element_visible(self.CONFIRMATION_IMAGE)

    def click_back_home_button(self):
        """Click the 'Back Home' button"""
        element=self.wait.for_element_clickable(self.BACK_HOME_BUTTON)
        element.click()

