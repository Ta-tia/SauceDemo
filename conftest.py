import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture
def driver():
    """Create and return a webdriver"""
    options=Options()
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        },
    )
    options.add_argument("--disable-features=SafeBrowsing,PasswordLeakToggleMove")
    driver=webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def logged_in(driver):
    """Return a driver already logged in as standard user"""
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    yield driver

@pytest.fixture
def logged_in_with_item_in_cart(logged_in):
    inventory_page=InventoryPage(logged_in)
    inventory_page.add_product_to_cart_by_index(0)
    inventory_page.click_shopping_cart()
    inventory_page.click_checkout_button()
    yield logged_in

@pytest.fixture
def logged_in_with_three_items_in_cart(logged_in):
    inventory_page=InventoryPage(logged_in)
    inventory_page.add_product_to_cart_by_index(0)
    inventory_page.add_product_to_cart_by_index(2)
    inventory_page.add_product_to_cart_by_index(3)
    inventory_page.click_shopping_cart()
    inventory_page.click_checkout_button()
    yield logged_in

