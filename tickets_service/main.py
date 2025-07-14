from fastapi import FastAPI
from routes import tickets

app = FastAPI()

app.include_router(tickets.router, prefix="/api/v1/tickets", tags=["tickets"])