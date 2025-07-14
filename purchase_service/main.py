from fastapi import FastAPI
from routes import purchases

app = FastAPI(title="Purchase Microservice")

app.include_router(purchases.router, prefix="/api/v1/purchases", tags=["Compras"])