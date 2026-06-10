from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer)
    product = Column(String)
    amount = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)