import time
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_successful_login(driver):
    """Test login with valid credentials"""
    login_page=LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(driver)
    page_title = inventory_page.get_page_title()
    assert inventory_page.is_page_loaded(), "Login Failed"
    print("valid login test passed")


def test_invalid_login(driver):
    """Test login with invalid credentials"""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("invalid_user", "wrong_password")
    assert login_page.is_error_displayed(), "Error message should be displayed"
    error_text=login_page.get_error_message()
    assert "do not match" in error_text.lower(), "Error message incorrect"
    print("invalid login test passed")




def test_locked_user(driver):
    """Test login with locked out user"""

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    assert login_page.is_error_displayed(), "Error message should be displayed"
    error_text=login_page.get_error_message()
    assert error_text is not None, "Error text was None"
    assert "locked out" in error_text.lower(), "Lock out message incorrect"

    print("Locked out user test passed")



def test_empty_credentials(driver):
    """Test login with empty username and password"""

    login_page = LoginPage(driver)
    login_page.open()
    login_page.click_login_button()

    assert login_page.is_error_displayed(), "Error message should be displayed"
    error_text = login_page.get_error_message()
    assert error_text is not None, "Error text was None"
    assert "username is required" in error_text.lower(), "Username required message incorrect"

    print("Empty credentials test passed")

