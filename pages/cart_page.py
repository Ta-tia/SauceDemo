from selenium.webdriver.common.by import By
from utils.wait import  Wait

class CartPage:
    #Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    REMOVE_ITEM_BUTTON = (By.CLASS_NAME, "cart_button")
    CONTINUE_SHOPPING = (By.CLASS_NAME, "continue_shopping")



    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = Wait(driver)

    def wait_for_page(self):
        """Wait until the cart page is loaded."""
        element = self.wait.for_element_visible(self.CHECKOUT_BUTTON)


    def get_cart_item_names(self):
        """Return list of product names in cart."""
        elements = self.wait.for_elements_present(self.ITEM_NAME)
        # list_of_elements = []
        # for element in elements:
        #     list_of_elements.append((element.text))
        # return list_of_elements
        #
        return [element.text for element in elements]

    def get_cart_quantity(self):
        items=self.get_cart_item_names()
        return len(items)


    def click_checkout(self):
        """Click Checkout button."""
        element=self.wait.for_element_clickable(self.CHECKOUT_BUTTON)
        element.click()
