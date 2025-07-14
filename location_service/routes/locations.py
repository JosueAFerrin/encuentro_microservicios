from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal
from schemas.location import LocationCreate, LocationUpdate, LocationOut
from services.location_service import (
    get_all_locations, get_location_by_id,
    create_location, update_location, delete_location
)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[LocationOut])
def list_locations(db: Session = Depends(get_db)):
    return get_all_locations(db)

@router.get("/{location_id}", response_model=LocationOut)
def get_location(location_id: int, db: Session = Depends(get_db)):
    location = get_location_by_id(db, location_id)
    if not location:
        raise HTTPException(status_code=404, detail="Ubicación no encontrada")
    return location

@router.post("/", response_model=LocationOut)
def create_new_location(location: LocationCreate, db: Session = Depends(get_db)):
    return create_location(db, location)

@router.put("/{location_id}", response_model=LocationOut)
def update_existing_location(location_id: int, location: LocationUpdate, db: Session = Depends(get_db)):
    return update_location(db, location_id, location)

@router.delete("/{location_id}")
def delete_existing_location(location_id: int, db: Session = Depends(get_db)):
    result = delete_location(db, location_id)
    if not result:
        raise HTTPException(status_code=404, detail="Ubicación no encontrada")
    return {"detail": "Ubicación eliminada"}