from selenium.webdriver.common.by import By
from utils.wait import  Wait

class InventoryPage:
    """Page Object for the Inventory/products page """

    URL="https://www.saucedemo.com/inventory.html"

    #Locators
    PAGE_TITLE=(By.CLASS_NAME, "title")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    PRODUCT_DESCRIPTIONS = (By.CLASS_NAME, "inventory_item_desc")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button[id^='add-to-cart']")
    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CHECKOUT_BUTTON = (By.CLASS_NAME, "checkout_button")


    def __init__(self, driver, timeout=10):
        self.driver=driver
        self.wait=Wait(driver)

    def open(self):
        """Open the webpage"""
        self.driver.get(self.URL)
        self.wait.for_element_visible(self.PAGE_TITLE)

    def get_page_title(self):
        """Get the page title text"""
        element = self.wait.for_element_visible(self.PAGE_TITLE)
        return element.text

    def is_page_loaded(self):
        """Verify that inventory text is loaded"""
        try:
            element = self.wait.for_element_visible(self.PAGE_TITLE, timeout=5)
            return "products" in element.text.lower()
        except:
            return False

    def get_product_names(self):
        """Get a list of all product names"""
        elements = self.wait.for_elements_present(self.PRODUCT_NAMES)
        return [element.text for element in elements]

    def get_product_count(self):
        """Get the number of products displayed"""
        elements = self.wait.for_elements_present(self.PRODUCT_ITEMS)
        return len(elements)

    def get_product_prices(self):
        """Get the list of all product prices"""
        elements = self.wait.for_elements_present(self.PRODUCT_PRICES)
        return [element.text for element in elements]

    def get_product_descriptions(self):
        """Get the list of all product descriptions"""
        elements = self.wait.for_elements_present(self.PRODUCT_DESCRIPTIONS)
        return [element.text for element in elements]

    def get_product_info(self):
        """Get detailed information for all products"""
        names = self.get_product_names()
        prices = self.get_product_prices()
        descriptions=self.get_product_descriptions()

        return [
            {"name": names[i], "price": prices[i], "description": descriptions[i]}
            for i in range(len(names))
        ]


    def click_product_by_name(self, product_name):
        """Click a product by name"""
        elements = self.wait.for_elements_present(self.PRODUCT_NAMES)
        for element in elements:
            if element.text == product_name:
                element.click()
                return True
        return False

    def click_first_product(self):
        """Click on the first product"""
        try:
            elements=self.wait.for_elements_present(self.PRODUCT_NAMES)
            if elements:
                self.wait.for_element_clickable(self.PRODUCT_NAMES)
                elements[0].click()
                return True
            return False
        except:
            return False

    def add_product_to_cart_by_index(self, index):
        """Add product to cart by index"""
        buttons=self.wait.for_elements_present(self.ADD_TO_CART_BUTTONS)
        if 0 <= index < len(buttons):
            buttons[index].click()
        else:
            raise ValueError(f"Index {index} is out of range")

    def click_shopping_cart(self):
        """Click on the shopping cart icon"""
        element=self.wait.for_element_clickable(self.SHOPPING_CART)
        element.click()

    def get_cart_item_count(self):
        """Get number of items in cart"""
        try:
            badge = self.wait.for_element_visible(self.SHOPPING_CART_BADGE, timeout=2)
            return int(badge.text)
        except:
            return 0

    def click_checkout_button(self):
        """Click on the checkout button"""
        element = self.wait.for_element_clickable(self.CHECKOUT_BUTTON)
        element.click()
