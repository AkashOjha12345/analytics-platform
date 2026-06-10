from sqlalchemy import Column, Integer, Float
from app.database import Base

class Refund(Base):
    __tablename__ = "refunds"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer)
    refunds = Column(Float)