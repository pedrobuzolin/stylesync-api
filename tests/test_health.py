def test_index(client):
    response = client.get("/")

    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Bem vindo ao StyleSync!"