import os
from dotenv import load_dotenv
import pytest

load_dotenv()

@pytest.mark.api
@pytest.mark.regression
def test_patch_post(api_client):

    # Get API base URL
    base_url = os.getenv("JSONPLACEHOLDER_BASE_URL")

    # Prepare partial update data
    patch_data = {
        "title": "My Updated Title"
    }

    # Send PATCH request
    response = api_client.patch(
        f"{base_url}/posts/1",
        data=patch_data
    )

    # Verify status code
    assert response.status == 200

    # Convert response into JSON
    response_data = response.json()

    # Verify updated title
    assert response_data["title"] == patch_data["title"]