import os
import pytest
from dotenv import load_dotenv

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

load_dotenv()


def login_to_saucedemo(page):
    login = LoginPage(page)

    login.open(os.getenv("SAUCEDEMO_BASE_URL"))
    login.enter_username(os.getenv("SAUCEDEMO_USERNAME"))
    login.enter_password(os.getenv("SAUCEDEMO_PASSWORD"))
    login.click_login()


@pytest.mark.ui
@pytest.mark.regression
def test_sort_products_a_to_z(page):
    login_to_saucedemo(page)

    inventory = InventoryPage(page)
    inventory.sort_products("az")

    names = inventory.get_product_names()

    assert names == sorted(names)


@pytest.mark.ui
@pytest.mark.regression
def test_sort_products_price_low_to_high(page):
    login_to_saucedemo(page)

    inventory = InventoryPage(page)
    inventory.sort_products("lohi")

    prices = inventory.get_product_prices()

    assert prices == sorted(prices)


@pytest.mark.ui
@pytest.mark.regression
def test_add_product_to_cart(page):
    login_to_saucedemo(page)

    inventory = InventoryPage(page)
    inventory.add_backpack_to_cart()
    inventory.open_cart()

    cart = CartPage(page)

    assert "Sauce Labs Backpack" in cart.get_cart_items()


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
def test_complete_checkout(page):
    login_to_saucedemo(page)

    inventory = InventoryPage(page)
    inventory.add_backpack_to_cart()
    inventory.open_cart()

    cart = CartPage(page)
    assert "Sauce Labs Backpack" in cart.get_cart_items()

    cart.click_checkout()

    checkout = CheckoutPage(page)
    checkout.enter_customer_details(
        "Kruti",
        "Gupta",
        "411001"
    )
    checkout.click_continue()
    checkout.finish_order()

    assert checkout.get_confirmation_message() == "Thank you for your order!"