from sqlalchemy.orm import Session
from models import Event
from schemas.event import EventCreate, EventUpdate

def get_all_events(db: Session):
    return db.query(Event).all()

def get_event_by_id(db: Session, event_id: int):
    return db.query(Event).filter(Event.id == event_id).first()

def create_event(db: Session, event: EventCreate):
    db_event = Event(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def update_event(db: Session, event_id: int, event: EventUpdate):
    db_event = get_event_by_id(db, event_id)
    if db_event:
        for key, value in event.dict().items():
            setattr(db_event, key, value)
        db.commit()
        db.refresh(db_event)
    return db_event

def delete_event(db: Session, event_id: int):
    db_event = get_event_by_id(db, event_id)
    if db_event:
        db.delete(db_event)
        db.commit()
    return db_event