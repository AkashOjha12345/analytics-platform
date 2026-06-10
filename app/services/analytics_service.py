from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.order import Order


def total_sales(db: Session):

    total = db.query(
        func.sum(Order.amount)
    ).scalar()

    return total