from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.customer import Customer
from app.models.order import Order
from app.models.refund import Refund

router = APIRouter(prefix="/mock", tags=["Mock APIs"])


@router.get("/customers")
def get_customers(
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_db)
):

    skip = (page - 1) * page_size

    customers = (
        db.query(Customer)
        .offset(skip)
        .limit(page_size)
        .all()
    )

    return {
        "page": page,
        "page_size": page_size,
        "data": customers
    }

@router.get("/orders")
def get_orders(
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_db)
):

    skip = (page - 1) * page_size

    orders = (
        db.query(Order)
        .offset(skip)
        .limit(page_size)
        .all()
    )

    return {
        "page": page,
        "page_size": page_size,
        "data": orders
    }

@router.post("/orders")
def create_order(data: dict, db: Session = Depends(get_db)):

    order = Order(
        customer_id=data["customer_id"],
        product=data["product"],
        amount=data["amount"]
    )

    db.add(order)
    db.commit()

    return {"message": "Order added"}

@router.get("/refunds")
def get_refunds(
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_db)
):

    skip = (page - 1) * page_size

    refunds = (
        db.query(Refund)
        .offset(skip)
        .limit(page_size)
        .all()
    )

    return {
        "page": page,
        "page_size": page_size,
        "data": refunds
    }