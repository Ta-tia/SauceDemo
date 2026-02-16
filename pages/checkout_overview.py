from selenium.webdriver.common.by import By
from utils.wait import  Wait


class CheckoutOverview:
    #Locators
    TITLE = (By.XPATH, "//span[@data-test='title' and text()='Checkout: Overview']")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_QUANTITY = (By.CLASS_NAME, "cart_quantity")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX = (By.CLASS_NAME, "summary_tax_label")
    TOTAL_PRICE = (By.CLASS_NAME, "summary_total_label")
    CANCEL_BUTTON = (By.CLASS_NAME, "cart_cancel_link")
    FINISH_BUTTON = (By.CLASS_NAME, "cart_button")

    def __init__(self, driver, timeout=10):
        self.driver=driver
        self.wait=Wait(driver)

    def is_page_loaded(self):
        """Verify that cart page is loaded"""
        try:
            element = self.wait.for_element_visible(self.TITLE, timeout=5)
            return "checkout: overview" in element.text.lower()
        except:
            return ""

    def get_item_price(self):
        """Get prices of individual items"""
        prices=[]
        elements = self.wait.for_element_present(self.ITEM_PRICE)
        for element in elements:
            prices.append(element.text)
        return prices

    def get_tax(self):
        """Get the tax amount"""
        element = self.wait.for_element_visible(self.TAX)
        return element.text

    def get_total_price(self):
        """Get the Price Total for all items, including tax"""
        element = self.wait.for_element_visible(self.TOTAL_PRICE)
        return element.text

    def calculate_total(self):
        pass

    def click_finish(self):
        self.wait.for_element_clickable(self.FINISH_BUTTON)

