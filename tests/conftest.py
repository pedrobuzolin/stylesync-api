import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app(testing=True)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def create_test_user(client):
    user_data = {
        "username": "testadmin",
        "password": "123"
    }

    user = client.post("/user", json=user_data)

    return user_data

@pytest.fixture
def authenticated_headers(client, create_test_user):
    login = client.post("/login", json=create_test_user)
    token = login.json["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    return headers