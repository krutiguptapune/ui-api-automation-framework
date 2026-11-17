import os
from dotenv import load_dotenv
from pages.login_page import LoginPage


load_dotenv()


def test_valid_login(page):

    # Create LoginPage object
    login = LoginPage(page)

    # Open SauceDemo
    login.open(os.getenv("SAUCEDEMO_BASE_URL"))

    # Enter login credentials
    login.enter_username(os.getenv("SAUCEDEMO_USERNAME"))
    login.enter_password(os.getenv("SAUCEDEMO_PASSWORD"))

    # Click Login
    login.click_login()

    # Verify successful login
    assert page.locator('[data-test="title"]').inner_text() == "Products"