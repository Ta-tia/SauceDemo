from pages.checkout_your_information import CheckoutYourInformation
from pages.checkout_overview import CheckoutOverview
from time import sleep

# Verify that error is shown when clicking on continue with mandatory fields
# Verify that clicking on 'cancel' navigates back to cart
# Test positive flow and verify that clicking on continue brings to checkout overview page

def test_successful_navigation_to_checkout_overview(logged_in_with_item_in_cart):
    checkout_page = CheckoutYourInformation(logged_in_with_item_in_cart)
    checkout_overview_page = CheckoutOverview(logged_in_with_item_in_cart)
    checkout_page.fill_checkout_form("test", "test1", "08912")
    checkout_page.click_continue_button()
    assert checkout_overview_page.is_page_loaded(), "Checkout Failed"
    print("Valid checkout test passed")

def test_mandatory_fields(logged_in_with_item_in_cart):
    checkout_page = CheckoutYourInformation(logged_in_with_item_in_cart)
    checkout_page.click_continue_button()
    assert checkout_page.is_error_displayed(), "Error message should be displayed"
    error_text=checkout_page.get_error_message()
    assert "required" in error_text.lower(), "Error message incorrect"
    print("test mandatory fields test passed")
