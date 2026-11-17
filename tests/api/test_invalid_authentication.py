import os
from dotenv import load_dotenv
import pytest

load_dotenv()

@pytest.mark.api
@pytest.mark.regression
def test_invalid_authentication(api_client):

    # Get API base URL
    base_url = os.getenv("RESTFUL_BOOKER_BASE_URL")

    # Prepare incorrect credentials
    credentials = {
        "username": "wrong_user",
        "password": "wrong_password"
    }

    # Send authentication request
    response = api_client.post(
        f"{base_url}/auth",
        data=credentials
    )

    # Verify response status
    assert response.status == 200

    # Convert response into JSON
    response_data = response.json()

    # Verify authentication failure
    assert response_data["reason"] == "Bad credentials"