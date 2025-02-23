# tests/test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_order():
    response = client.post("/orders/", json={
        "symbol": "AAPL",
        "price": 125,
        "quantity": 10,
        "order_type": "buy"
    })
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,  
        "symbol": "AAPL",
        "price": 125,
        "quantity": 10,
        "order_type": "buy"
    }

def test_get_orders():
    response = client.get("/orders/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Ensure the response is a list
