import json
import os
import pytest
from dotenv import load_dotenv
from jsonschema import validate

load_dotenv()


@pytest.mark.api
@pytest.mark.regression
def test_post_response_schema(api_client):

    # Get API URL
    base_url = os.getenv("JSONPLACEHOLDER_BASE_URL")

    # Send GET request
    response = api_client.get(f"{base_url}/posts/1")

    # Verify status
    assert response.status == 200

    # Get response data
    response_data = response.json()

    # Read expected schema
    with open("test_data/post_schema.json", "r") as file:
        schema = json.load(file)

    # Validate response against schema
    validate(
        instance=response_data,
        schema=schema
    )