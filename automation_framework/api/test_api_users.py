import pytest
from automation_framework.api.api_client import APIClient

@pytest.fixture
def api_client():
    return APIClient()

def test_get_users(api_client):
    response = api_client.get_users()
    assert response.status_code == 200
    users = response.json()
    assert len(users) > 0
    for user in users:
        assert "id" in user
        assert "name" in user
        assert "username" in user
        assert "email" in user

def test_create_post(api_client):
    title = "foo"
    body = "bar"
    user_id = 1
    response = api_client.create_post(title, body, user_id)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == title

def test_fail_create_post(api_client):
    title = "foo"
    body = "bar"
    user_id = "abc"
    response = api_client.create_post(title, body, user_id)
    assert response.status_code == 201 #Should fail
