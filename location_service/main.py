from fastapi import FastAPI
from routes import locations

app = FastAPI(title="Location Microservice")

app.include_router(locations.router, prefix="/api/v1/locations", tags=["Ubicaciones"])