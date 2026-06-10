import requests
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.customer import Customer
from app.models.order import Order
from app.models.refund import Refund


BASE_URL = "http://127.0.0.1:8000"


# ---------------------------------
# DATABASE SESSION
# ---------------------------------
db: Session = SessionLocal()


# ---------------------------------
# FETCH PAGINATED DATA
# ---------------------------------
def fetch_all_data(endpoint):

    page = 1
    page_size = 100

    all_data = []

    while True:

        url = f"{BASE_URL}/{endpoint}?page={page}&page_size={page_size}"

        response = requests.get(url)

        data = response.json()["data"]

        if not data:
            break

        all_data.extend(data)

        print(f"Fetched page {page} from {endpoint}")

        page += 1

    return all_data


# ---------------------------------
# INGEST CUSTOMERS
# ---------------------------------
def ingest_customers():

    customers = fetch_all_data("/mock/customers")

    for item in customers:

        customer = Customer(
            id=item["id"],
            name=item["name"],
            email=item["email"]
        )

        db.merge(customer)

    db.commit()

    print("Customers inserted")


# ---------------------------------
# INGEST ORDERS
# ---------------------------------
def ingest_orders():

    orders = fetch_all_data("/mock/orders")

    for item in orders:

        order = Order(
            id=item["id"],
            customer_id=item["customer_id"],
            product=item["product"],
            amount=item["amount"]
        )

        db.merge(order)

    db.commit()

    print("Orders inserted")


# ---------------------------------
# INGEST REFUNDS
# ---------------------------------
def ingest_refunds():

    refunds = fetch_all_data("/mock/refunds")

    for item in refunds:

        refund = Refund(
            id=item["id"],
            order_id=item["order_id"],
            reason=item["reason"]
        )

        db.merge(refund)

    db.commit()

    print("Refunds inserted")


# ---------------------------------
# MAIN
# ---------------------------------
if __name__ == "__main__":

    ingest_customers()
    ingest_orders()
    ingest_refunds()

    print("Data ingestion completed")