import time
import os
from dotenv import load_dotenv

load_dotenv()


def test_get_single_post(api_request_context):

    # Get API base URL
    base_url = os.getenv("JSONPLACEHOLDER_BASE_URL")

    # Start measuring response time
    start_time = time.time()

    # Send GET request
    response = api_request_context.get(
        f"{base_url}/posts/1"
    )

    # Calculate response time in milliseconds
    response_time = (time.time() - start_time) * 1000

    # Verify response time
    assert response_time < 3000

    # Verify status code
    assert response.status == 200

    # Verify response content type
    assert "application/json" in response.headers["content-type"]

    # Convert response into JSON
    response_data = response.json()

    # Verify response data
    assert response_data["id"] == 1
    assert response_data["userId"] == 1
    assert "title" in response_data
    assert "body" in response_data

    # Verify response data types
    assert isinstance(response_data["id"], int)
    assert isinstance(response_data["userId"], int)
    assert isinstance(response_data["title"], str)
    assert isinstance(response_data["body"], str)