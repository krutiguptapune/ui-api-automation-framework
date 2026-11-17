import os
from dotenv import load_dotenv

load_dotenv()


def test_update_post(api_request_context):

    # Get API base URL
    base_url = os.getenv("JSONPLACEHOLDER_BASE_URL")

    # Prepare updated post data
    updated_data = {
        "id": 1,
        "title": "Updated Post",
        "body": "Learning API Automation",
        "userId": 1
    }

    # Send PUT request
    response = api_request_context.put(
        f"{base_url}/posts/1",
        data=updated_data
    )

    # Verify status code
    assert response.status == 200

    # Convert response into JSON
    response_data = response.json()

    # Verify updated information
    assert response_data["id"] == 1
    assert response_data["title"] == updated_data["title"]
    assert response_data["body"] == updated_data["body"]
    assert response_data["userId"] == updated_data["userId"]