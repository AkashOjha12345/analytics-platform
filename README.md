# analytics-platform
# Analytics Platform

A scalable backend analytics platform built using FastAPI, PostgreSQL, and SQLAlchemy.

## Features

* Mock APIs
* Pagination Support
* Data Ingestion Service
* PostgreSQL Integration
* Analytics APIs
* Revenue Metrics
* Large Dataset Processing

---

# Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Faker

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/AkashOjha12345/analytics-platform.git
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

## 3. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Configure PostgreSQL

Create PostgreSQL database:

```sql
CREATE DATABASE analytics_db;
```

Update database connection inside:

```text
app/database.py
```

---

# Run Application

```bash
uvicorn app.main:app --reload
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# Generate Fake Data

```bash
python -m app.utils.data_generator
```

---

# Run Ingestion Service

```bash
python -m app.services.ingestion_service
```

# API Documentation

## Customer APIs

### Get Customers

```http
GET /mock/customers?page=1&page_size=10
```

---

## Orders APIs

### Get Orders

```http
GET /mock/orders?page=1&page_size=10
```

### Create Order

```http
POST /mock/orders
```

Body:

```json
{
  "customer_id": 1,
  "product": "Laptop",
  "amount": 5000
}
```

---

## Refund APIs

### Get Refunds

```http
GET /mock/refunds?page=1&page_size=10
```

---

# Analytics APIs

## Total Orders

```http
GET /analytics/total-orders
```

## Total Revenue

```http
GET /analytics/total-revenue
```

## Total Refunds

```http
GET /analytics/total-refunds
```

## Net Revenue

```http
GET /analytics/net-revenue
```

## Average Order Value

```http
GET /analytics/average-order-value
```

## Repeat Customer Revenue

```http
GET /analytics/repeat-customer-revenue
```

## Revenue Trends

```http
GET /revenue-trends
```

## Top Customers

```http
GET /top-customers
```
