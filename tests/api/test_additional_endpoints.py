import os
import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.mark.api
@pytest.mark.regression
def test_get_all_posts(api_client):
    base_url = os.getenv("JSONPLACEHOLDER_BASE_URL")

    response = api_client.get(f"{base_url}/posts")

    assert response.status == 200

    posts = response.json()

    assert isinstance(posts, list)
    assert len(posts) > 0


@pytest.mark.api
@pytest.mark.regression
def test_get_post_comments(api_client):
    base_url = os.getenv("JSONPLACEHOLDER_BASE_URL")

    response = api_client.get(
        f"{base_url}/posts/1/comments"
    )

    assert response.status == 200

    comments = response.json()

    assert isinstance(comments, list)
    assert len(comments) > 0

    for comment in comments:
        assert comment["postId"] == 1
        assert "email" in comment
        assert "body" in comment


@pytest.mark.api
@pytest.mark.regression
def test_get_single_user(api_client):
    base_url = os.getenv("JSONPLACEHOLDER_BASE_URL")

    response = api_client.get(f"{base_url}/users/1")

    assert response.status == 200

    user = response.json()

    assert user["id"] == 1
    assert "name" in user
    assert "email" in user
    assert "username" in user


@pytest.mark.api
@pytest.mark.regression
def test_get_nonexistent_post(api_client):
    base_url = os.getenv("JSONPLACEHOLDER_BASE_URL")

    response = api_client.get(f"{base_url}/posts/9999")

    assert response.status == 404