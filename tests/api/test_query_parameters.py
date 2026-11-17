import os
from dotenv import load_dotenv

load_dotenv()


def test_get_posts_by_user(api_request_context):

    # Get API base URL
    base_url = os.getenv("JSONPLACEHOLDER_BASE_URL")

    # Send GET request with query parameter
    response = api_request_context.get(
        f"{base_url}/posts",
        params={"userId": 1}
    )

    # Verify status code
    assert response.status == 200

    # Convert response into JSON
    response_data = response.json()

    # Verify that posts were returned
    assert len(response_data) > 0

    # Verify every post belongs to user 1
    for post in response_data:
        assert post["userId"] == 1