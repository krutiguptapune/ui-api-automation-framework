import os
from dotenv import load_dotenv
import pytest

load_dotenv()

@pytest.mark.api
@pytest.mark.regression
def test_delete_post(api_client):

    # Get API base URL
    base_url = os.getenv("JSONPLACEHOLDER_BASE_URL")

    # Send DELETE request
    response = api_client.delete(
        f"{base_url}/posts/1"
    )

    # Verify status code
    assert response.status == 200