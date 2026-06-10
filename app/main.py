from fastapi import FastAPI
from app.routes import mock_api, analytics, health
from app.routes.analytics import router as analytics_router
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Analytics Platform API")

app.include_router(mock_api.router)
app.include_router(analytics.router)
app.include_router(health.router)
app.include_router(analytics_router, prefix="/analytics")

@app.get("/")
def home():
    return {"message": "Analytics Platform Running"}