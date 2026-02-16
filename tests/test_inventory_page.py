"""Test scenarios for inventory functionality"""
from pages.inventory_page import InventoryPage



def test_product_count(logged_in):
    """Test that 6 products are displayed"""

    inventory_page = InventoryPage(logged_in)
    count = inventory_page.get_product_count()

    assert count == 6, f"Expected 6 products, fount {count}"
    print("Product count test passed")




def test_product_names(logged_in):
    """Test that product names are retrieved correctly"""

    inventory_page = InventoryPage(logged_in)
    names = inventory_page.get_product_names()

    assert len(names) > 0, "No product names found"
    assert "Backpack" in names[0], "First product should be Backpack"

    print("✓ Product names test passed")




def test_add_to_cart(logged_in):
    """Test adding product to cart"""


    inventory_page = InventoryPage(logged_in)

    initial_count = inventory_page.get_cart_item_count()
    assert initial_count == 0, "Cart should be empty initially"

    inventory_page.add_product_to_cart_by_index(0)

    cart_count = inventory_page.get_cart_item_count()
    assert cart_count == 1, f"Expected 1 item in cart, found {cart_count}"

    print("✓ Add to cart test passed")



def test_add_multiple_products(logged_in):
    """Test adding multiple products to cart"""


    inventory_page = InventoryPage(logged_in)

    inventory_page.add_product_to_cart_by_index(0)
    inventory_page.add_product_to_cart_by_index(1)
    inventory_page.add_product_to_cart_by_index(2)

    cart_count = inventory_page.get_cart_item_count()
    assert cart_count == 3, f"Expected 3 items in cart, found {cart_count}"

    print("✓ Multiple products test passed")




def test_product_prices(logged_in):
    """Test that product prices are displayed"""

    inventory_page = InventoryPage(logged_in)
    prices = inventory_page.get_product_prices()

    assert len(prices) == 6, f"Expected 6 prices, found {len(prices)}"

    for price in prices:
        assert "$" in price, f"Price {price} should contain $"
        assert len(price) > 1, f"Price {price} is invalid"

    print("✓ Product prices test passed")



def test_click_product(logged_in):
    """Test clicking on a product"""

    inventory_page = InventoryPage(logged_in)
    result = inventory_page.click_first_product()

    assert result, "Failed to click first product"
    assert "inventory-item" in logged_in.current_url, "Should navigate to product page"

    print("✓ Click product test passed")



