"""LoginPage - Page Object for SauceDemo login page"""
from selenium.webdriver.common.by import By
from utils.wait import  Wait

class LoginPage:
    """Page Object for the Login Page"""

    URL="https://www.saucedemo.com/"

    #Locators
    USERNAME_INPUT=(By.ID, "user-name")
    PASSWORD_INPUT=(By.ID, "password")
    LOGIN_BUTTON=(By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver=driver
        self.wait=Wait(driver)

    def open(self):
        self.driver.get(self.URL)
        self.wait.for_element_visible(self.USERNAME_INPUT)

    def user_name_input(self, username):
        """Enter username into the username field"""
        element = self.wait.for_element_visible(self.USERNAME_INPUT)
        element.clear()
        element.send_keys(username)

    def password_input(self, password):
        """Enter password into the password field"""
        element = self.wait.for_element_visible(self.PASSWORD_INPUT)
        element.clear()
        element.send_keys(password)

    def click_login_button(self):
        """Click the login button"""
        self.wait.for_element_clickable(self.LOGIN_BUTTON).click()


    def login(self, username, password):
        """Perform complete login action"""
        self.user_name_input(username)
        self.password_input(password)
        self.click_login_button()

    def get_error_message(self):
        """Get error message text if present"""
        try:
            element = self.wait.for_element_visible(self.ERROR_MESSAGE, timeout=3)
            return element.text
        except:
            return ""

    def is_error_displayed(self):
        """Check if the error message is displayed"""
        try:
            self.wait.for_element_visible(self.ERROR_MESSAGE, timeout=3)
            return True
        except:
            return False

    def get_login_button_value(self):
        """Get the text of the login button"""

        return self.driver.find_element(*self.LOGIN_BUTTON).get_attribute("value")

