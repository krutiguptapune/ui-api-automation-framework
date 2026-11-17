import os
from dotenv import load_dotenv
import pytest

load_dotenv()

@pytest.mark.api
def test_delete_post(api_request_context):

    # Get API base URL
    base_url = os.getenv("JSONPLACEHOLDER_BASE_URL")

    # Send DELETE request
    response = api_request_context.delete(
        f"{base_url}/posts/1"
    )

    # Verify status code
    assert response.status == 200