import json
import os
import pytest
from dotenv import load_dotenv
from pages.login_page import LoginPage


load_dotenv()


# Read login scenarios from JSON
with open("test_data/login_data.json", "r") as file:
    login_data = json.load(file)

@pytest.mark.ui
@pytest.mark.parametrize("scenario", login_data)
@pytest.mark.regression
def test_invalid_login(page, scenario):

    # Create LoginPage object
    login = LoginPage(page)

    # Open SauceDemo
    login.open(os.getenv("SAUCEDEMO_BASE_URL"))

    # Enter username and password
    login.enter_username(scenario["username"])
    login.enter_password(scenario["password"])

    # Click Login
    login.click_login()

    # Get and verify error message
    error_message = login.get_error_message()

    assert error_message == scenario["expected_error"]