from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db
from app.models.order import Order
from app.models.refund import Refund

router = APIRouter()


# -----------------------------------
# TOTAL ORDERS
# -----------------------------------
@router.get("/total-orders")
def total_orders(db: Session = Depends(get_db)):

    total = db.query(func.count(Order.id)).scalar()

    return {
        "total_orders": total
    }


# -----------------------------------
# TOTAL REVENUE
# -----------------------------------
@router.get("/total-revenue")
def total_revenue(db: Session = Depends(get_db)):

    revenue = db.query(func.sum(Order.amount)).scalar()

    return {
        "total_revenue": revenue
    }


# -----------------------------------
# TOTAL REFUNDS
# -----------------------------------
@router.get("/total-refunds")
def total_refunds(db: Session = Depends(get_db)):

    refunds = db.query(func.count(Refund.id)).scalar()

    return {
        "total_refunds": refunds
    }


# -----------------------------------
# NET REVENUE
# -----------------------------------
@router.get("/net-revenue")
def net_revenue(db: Session = Depends(get_db)):

    total_revenue = db.query(func.sum(Order.amount)).scalar() or 0

    refunded_amount = (
        db.query(func.sum(Order.amount))
        .join(Refund, Refund.order_id == Order.id)
        .scalar()
    ) or 0

    net = total_revenue - refunded_amount

    return {
        "net_revenue": net
    }


# -----------------------------------
# AVERAGE ORDER VALUE
# -----------------------------------
@router.get("/average-order-value")
def average_order_value(db: Session = Depends(get_db)):

    avg = db.query(func.avg(Order.amount)).scalar()

    return {
        "average_order_value": round(avg, 2)
    }


# -----------------------------------
# REPEAT CUSTOMER REVENUE
# -----------------------------------
@router.get("/repeat-customer-revenue")
def repeat_customer_revenue(db: Session = Depends(get_db)):

    subquery = (
        db.query(Order.customer_id)
        .group_by(Order.customer_id)
        .having(func.count(Order.id) > 1)
        .subquery()
    )

    revenue = (
        db.query(func.sum(Order.amount))
        .filter(Order.customer_id.in_(subquery))
        .scalar()
    )

    return {
        "repeat_customer_revenue": revenue
    }


# -----------------------------------
# REVENUE TRENDS
# -----------------------------------
@router.get("/revenue-trends")
def revenue_trends(db: Session = Depends(get_db)):

    trends = (
        db.query(
            func.date(Order.created_at).label("date"),
            func.sum(Order.amount).label("revenue")
        )
        .group_by(func.date(Order.created_at))
        .all()
    )

    result = []

    for trend in trends:
        result.append({
            "date": str(trend.date),
            "revenue": float(trend.revenue)
        })

    return result


# -----------------------------------
# TOP CUSTOMERS BY SPEND
# -----------------------------------
@router.get("/top-customers")
def top_customers(db: Session = Depends(get_db)):

    customers = (
        db.query(
            Order.customer_id,
            func.sum(Order.amount).label("total_spend")
        )
        .group_by(Order.customer_id)
        .order_by(func.sum(Order.amount).desc())
        .limit(10)
        .all()
    )

    result = []

    for customer in customers:
        result.append({
            "customer_id": customer.customer_id,
            "total_spend": float(customer.total_spend)
        })

    return result

   