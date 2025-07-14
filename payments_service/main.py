from fastapi import FastAPI
from routes import payments

app = FastAPI()
app.include_router(payments.router, prefix="/api/v1/payments", tags=["Payments"])
