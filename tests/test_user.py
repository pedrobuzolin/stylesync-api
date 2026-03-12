def test_get_users_authorized(client, authenticated_headers):
    response = client.get("/users", headers=authenticated_headers)

    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_get_users_without_token(client):
    response = client.get("/users")

    assert response.status_code == 401

def test_get_users_with_invalid_token(client):
    response = client.get("/users", headers={"Authorization": "Bearer ivalidtoken"})

    assert response.status_code == 401

def test_create_user_sucess(client):
    user_data = {
        "username": "test",
        "password": "abcd"
    }

    response = client.post("/users", json=user_data)

    assert response.status_code == 201
    data = response.get_json()
    assert data["message"] == "Usuario cadastrado com sucesso!"

def test_create_user_with_invalid_data(client):
    user_data = {
        "username": "test",
        "pass": 123.4
    }

    response = client.post("/users", json=user_data)

    assert response.status_code == 400