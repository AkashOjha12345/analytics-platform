import random
import psycopg2
from faker import Faker

DB_CONFIG = {
    "host": "localhost",
    "database": "analytics_db",
    "user": "postgres",
    "password": "user",
    "port": 5432
}

fake = Faker()
conn = psycopg2.connect(**DB_CONFIG)
cursor = conn.cursor()

print("✅ Database connected successfully")

BATCH_SIZE = 5000

# -----------------------------
# CUSTOMERS
# -----------------------------
def insert_customers(n=100000):
    batch = []

    for i in range(n):
        batch.append((
            random.randint(1, 100000),
            fake.name(),
            fake.email()
                              
        ))

        if len(batch) == BATCH_SIZE:
            cursor.executemany("""
                INSERT INTO customer (id,name, email)
                VALUES (%s,%s, %s)
            """, batch)
            conn.commit()
            batch = []

    if batch:
        cursor.executemany("""
            INSERT INTO customer (id,name, email)
            VALUES (%s,%s, %s)
        """, batch)
        conn.commit()

    print("Customers inserted")


# -----------------------------
# ORDERS
# -----------------------------
def insert_orders(n=1000000):
    batch = []
    products = [
    "Laptop",
    "Phone",
    "Keyboard",
    "Mouse",
    "Monitor",
    "Camera",
    "Tablet"
    ]

    for i in range(n):
        batch.append((
            random.randint(1, 100000),
            random.choice(products),
            round(random.uniform(100, 5000), 2)
        ))

        if len(batch) == BATCH_SIZE:
            cursor.executemany("""
                INSERT INTO orders (customer_id, product, amount)
                VALUES (%s, %s, %s)
            """, batch)
            conn.commit()
            batch = []

    if batch:
        cursor.executemany("""
            INSERT INTO orders (customer_id, product , amount)
            VALUES (%s, %s, %s)
        """, batch)
        conn.commit()

    print("Orders inserted")


# -----------------------------
# REFUNDS
# -----------------------------
def insert_refunds(n=200000):
    batch = []

    for i in range(n):
        batch.append((
            random.randint(1, 1000000),
            round(random.uniform(50, 2000), 2)
        ))

        if len(batch) == BATCH_SIZE:
            cursor.executemany("""
                INSERT INTO refunds (order_id, refunds)
                VALUES (%s, %s)
            """, batch)
            conn.commit()
            batch = []

    if batch:
        cursor.executemany("""
            INSERT INTO refunds (order_id, refunds)
            VALUES (%s, %s)
        """, batch)
        conn.commit()

    print("Refunds inserted")


# -----------------------------
# RUN ALL
# -----------------------------
if __name__ == "__main__":
    insert_customers()
    insert_orders()
    insert_refunds()

    cursor.close()
    conn.close()

    print("ALL DATA GENERATED 🚀")