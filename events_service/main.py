from fastapi import FastAPI
from routes import events

app = FastAPI(title="Events Microservice")

app.include_router(events.router, prefix="/api/v1/eventos", tags=["Eventos"])