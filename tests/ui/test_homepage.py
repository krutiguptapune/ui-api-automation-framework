import os
from dotenv import load_dotenv


load_dotenv()


def test_saucedemo_homepage(page):
    # Open SauceDemo website
    page.goto(os.getenv("SAUCEDEMO_BASE_URL"))

    # Check whether the page title is correct
    assert page.title() == "Swag Labs"