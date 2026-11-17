import os
from dotenv import load_dotenv
import pytest


load_dotenv()

@pytest.mark.ui
@pytest.mark.smoke
def test_saucedemo_homepage(page):
    # Open SauceDemo website
    page.goto(os.getenv("SAUCEDEMO_BASE_URL"))

    # Check whether the page title is correct
    assert page.title() == "Swag Labs"