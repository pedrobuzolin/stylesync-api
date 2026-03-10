import io

def test_upload_sales_success(client, authenticated_headers):
    csv_content = """date,product,quantity,price
    2025-01-01,produto a,2,10.50
    2025-01-02,produto b,4,5.40
    """

    data = {
        "file": (io.BytesIO(csv_content.encode()), "sales.csv")
    }    

    response = client.post(
        "/sales/upload",
        data=data,
        headers=authenticated_headers,
        content_type="multipart/form-data"
    )
    
    assert response.status_code == 200

def test_upload_sales_without_file(client, authenticated_headers):
    response = client.post("/sales/upload", headers=authenticated_headers)

    assert response.status_code == 400