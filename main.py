# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Order, Base  # Import Order from models.py

app = FastAPI()

# Define SQLite database connection string
DATABASE_URL = "sqlite:///./test.db"

# Set up SQLAlchemy
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Pydantic model for the API input
class OrderCreate(BaseModel):
    symbol: str
    price: float  # Change price to float for more precision
    quantity: int
    order_type: str

# Pydantic model for the API output
class OrderResponse(BaseModel):
    id: int
    symbol: str
    price: float  # Change price to float for consistency
    quantity: int
    order_type: str

    class Config:
        orm_mode = True

# FastAPI endpoint to create orders
@app.post("/orders/", response_model=OrderResponse)
def create_order(order: OrderCreate):
    db = SessionLocal()
    db_order = Order(symbol=order.symbol, price=order.price, quantity=order.quantity, order_type=order.order_type)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    db.close()
    return db_order

# FastAPI endpoint to get all orders
@app.get("/orders/", response_model=list[OrderResponse])
def get_orders():
    db = SessionLocal()
    orders = db.query(Order).all()
    db.close()
    return orders
