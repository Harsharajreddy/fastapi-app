# tests/test_main.py
from fastapi.testclient import TestClient
from main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Order
import pytest

# Set up testing database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the tables for testing
Base.metadata.create_all(bind=engine)

client = TestClient(app)

@pytest.fixture
def db_session():
    # Create a new session for each test
    db = SessionLocal()
    yield db
    db.close()

def test_create_order(db_session):
    # Test creating an order
    order_data = {
        "symbol": "AAPL",
        "price": 125.35,  # Price with a decimal point
        "quantity": 10,
        "order_type": "buy"
    }
    response = client.post("/orders/", json=order_data)
    assert response.status_code == 200

def test_get_orders(db_session):
    # Cleanup: delete all orders before testing
    db_session.query(Order).delete()
    db_session.commit()

    # Test getting orders when no orders exist
    response = client.get("/orders/")
    assert response.status_code == 200
    assert response.json() == []  # Now it should return an empty list

    # Adding an order for subsequent tests
    db_session.add(Order(symbol="AAPL", price=125.35, quantity=10, order_type="buy"))
    db_session.commit()

    # Test getting orders after adding one
    response = client.get("/orders/")
    assert response.status_code == 200
    assert len(response.json()) == 1  # Now it should return 1 order
