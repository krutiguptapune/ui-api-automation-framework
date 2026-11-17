import json
import os
import pytest
from dotenv import load_dotenv

load_dotenv()

with open("test_data/api_test_data.json", "r") as file:
    test_data = json.load(file)


@pytest.mark.api
@pytest.mark.regression
@pytest.mark.parametrize("scenario", test_data)
def test_get_post_with_different_ids(api_client, scenario):

    base_url = os.getenv("JSONPLACEHOLDER_BASE_URL")

    response = api_client.get(
        f"{base_url}/posts/{scenario['post_id']}"
    )

    assert response.status == 200

    post = response.json()

    assert post["id"] == scenario["post_id"]
    assert post["userId"] == scenario["expected_user_id"]
    assert isinstance(post["title"], str)
    assert isinstance(post["body"], str)