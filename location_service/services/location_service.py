from sqlalchemy.orm import Session
from models import Location
from schemas.location import LocationCreate, LocationUpdate

def get_all_locations(db: Session):
    return db.query(Location).all()

def get_location_by_id(db: Session, location_id: int):
    return db.query(Location).filter(Location.id == location_id).first()

def create_location(db: Session, location: LocationCreate):
    db_location = Location(**location.dict())
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location

def update_location(db: Session, location_id: int, location: LocationUpdate):
    db_location = get_location_by_id(db, location_id)
    if db_location:
        for key, value in location.dict().items():
            setattr(db_location, key, value)
        db.commit()
        db.refresh(db_location)
    return db_location

def delete_location(db: Session, location_id: int):
    db_location = get_location_by_id(db, location_id)
    if db_location:
        db.delete(db_location)
        db.commit()
    return db_location