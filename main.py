# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    price = Column(Integer)
    quantity = Column(Integer)
    order_type = Column(String)

Base.metadata.create_all(bind=engine)

class OrderCreate(BaseModel):
    symbol: str
    price: int
    quantity: int
    order_type: str

class OrderResponse(BaseModel):
    id: int
    symbol: str
    price: int
    quantity: int
    order_type: str

    class Config:
        orm_mode = True

@app.post("/orders/", response_model=OrderResponse)
def create_order(order: OrderCreate):
    db = SessionLocal()
    db_order = Order(symbol=order.symbol, price=order.price, quantity=order.quantity, order_type=order.order_type)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    db.close()
    return db_order

@app.get("/orders/", response_model=list[OrderResponse])
def get_orders():
    db = SessionLocal()
    orders = db.query(Order).all()
    db.close()
    return orders
