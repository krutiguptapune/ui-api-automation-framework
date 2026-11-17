import pytest
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.regression
def test_valid_authentication(api_client):

    # Get API base URL
    base_url = os.getenv("RESTFUL_BOOKER_BASE_URL")

    # Prepare login credentials
    credentials = {
        "username": os.getenv("RESTFUL_BOOKER_USERNAME"),
        "password": os.getenv("RESTFUL_BOOKER_PASSWORD")
    }

    # Send authentication request
    response = api_client.post(
        f"{base_url}/auth",
        data=credentials
    )

    # Verify status code
    assert response.status == 200

    # Convert response into JSON
    response_data = response.json()

    # Verify authentication token exists
    assert "token" in response_data

    # Verify token is not empty
    assert response_data["token"] != ""