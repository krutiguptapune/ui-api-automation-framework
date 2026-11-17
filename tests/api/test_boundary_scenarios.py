import os
import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.mark.api
@pytest.mark.regression
def test_get_last_post(api_client):
    base_url = os.getenv("JSONPLACEHOLDER_BASE_URL")

    response = api_client.get(f"{base_url}/posts/100")

    assert response.status == 200
    assert response.json()["id"] == 100


@pytest.mark.api
@pytest.mark.regression
def test_get_post_with_zero_id(api_client):
    base_url = os.getenv("JSONPLACEHOLDER_BASE_URL")

    response = api_client.get(f"{base_url}/posts/0")

    assert response.status == 404


@pytest.mark.api
@pytest.mark.regression
def test_get_post_with_negative_id(api_client):
    base_url = os.getenv("JSONPLACEHOLDER_BASE_URL")

    response = api_client.get(f"{base_url}/posts/-1")

    assert response.status == 404


@pytest.mark.api
@pytest.mark.regression
def test_get_comments_for_nonexistent_post(api_client):
    base_url = os.getenv("JSONPLACEHOLDER_BASE_URL")

    response = api_client.get(
        f"{base_url}/posts/9999/comments"
    )

    assert response.status == 200
    assert response.json() == []


@pytest.mark.api
@pytest.mark.regression
def test_get_all_users(api_client):
    base_url = os.getenv("JSONPLACEHOLDER_BASE_URL")

    response = api_client.get(f"{base_url}/users")

    assert response.status == 200

    users = response.json()

    assert len(users) == 10

    for user in users:
        assert "id" in user
        assert "name" in user
        assert "email" in user


@pytest.mark.api
@pytest.mark.regression
def test_get_post_response_content_type(api_client):
    base_url = os.getenv("JSONPLACEHOLDER_BASE_URL")

    response = api_client.get(f"{base_url}/posts/1")

    assert response.status == 200

    content_type = response.headers.get("content-type", "")

    assert "application/json" in content_type