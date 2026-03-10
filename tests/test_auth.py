def test_login_with_valid_credentials(client, create_test_user):
    response = client.post("/login", json=create_test_user)

    assert response.status_code == 200
    
    data = response.get_json()
    assert "access_token" in data

def test_login_with_wrong_password(client):
    user_data = {
        "username": "testadmin",
        "password": "abc"
    }

    response = client.post("/login", json=user_data)

    assert response.status_code == 404

def test_login_with_nonexistent_user(client):
    user_data = {
        "username": "teste",
        "password": "123"
    }

    response = client.post("/login", json=user_data)

    assert response.status_code == 404