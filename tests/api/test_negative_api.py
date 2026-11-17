import os
from dotenv import load_dotenv

load_dotenv()


def test_invalid_endpoint(api_request_context):

    # Get API base URL
    base_url = os.getenv("JSONPLACEHOLDER_BASE_URL")

    # Send request to an invalid endpoint
    response = api_request_context.get(
        f"{base_url}/invalid-endpoint"
    )

    # Verify that the endpoint was not found
    assert response.status == 404