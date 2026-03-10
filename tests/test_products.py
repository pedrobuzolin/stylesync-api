def test_get_products(client):
    response = client.get("/products")

    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_create_products_success(client, authenticated_headers):
    product_data = {
        "name": "Produto Teste",
        "price": 10.99,
        "description": "Produto de teste",
        "stock": 2
    }

    response = client.post("/products", json=product_data, headers=authenticated_headers)
    assert response.status_code == 201
    
    data = response.get_json()
    assert data["message"] == "Produto cadastrado com sucesso!"

def test_create_products_without_token(client):
    product_data = {
        "name": "Produto Teste",
        "price": 10.99,
        "description": "Produto de teste",
        "stock": 2
    }

    response = client.post("/products", json=product_data)
    assert response.status_code == 401