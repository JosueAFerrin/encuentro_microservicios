from fastapi import FastAPI
from routes import notifications

app = FastAPI(title="Notification Microservice")

app.include_router(notifications.router, prefix="/api/v1/notifications", tags=["Notificaciones"])