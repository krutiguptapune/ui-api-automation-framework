import os
from dotenv import load_dotenv
import pytest

load_dotenv()

@pytest.mark.api
@pytest.mark.regression
def test_create_post(api_request_context):

    # Get API base URL
    base_url = os.getenv("JSONPLACEHOLDER_BASE_URL")

    # Prepare post data
    post_data = {
        "title": "Learning API Automation",
        "body": "This is my first POST API test",
        "userId": 1
    }

    # Send POST request
    response = api_request_context.post(
        f"{base_url}/posts",
        data=post_data
    )

    # Verify status code
    assert response.status == 201

    # Convert response into JSON
    response_data = response.json()

    # Verify created post data
    assert response_data["title"] == post_data["title"]
    assert response_data["body"] == post_data["body"]
    assert response_data["userId"] == post_data["userId"]
    assert "id" in response_data