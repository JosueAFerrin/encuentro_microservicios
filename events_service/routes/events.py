from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal
from schemas.event import EventCreate, EventUpdate, EventOut
from services.event_service import (
    get_all_events, get_event_by_id,
    create_event, update_event, delete_event
)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[EventOut])
def list_events(db: Session = Depends(get_db)):
    return get_all_events(db)

@router.get("/{event_id}", response_model=EventOut)
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = get_event_by_id(db, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    return event

@router.post("/", response_model=EventOut)
def create_new_event(event: EventCreate, db: Session = Depends(get_db)):
    return create_event(db, event)

@router.put("/{event_id}", response_model=EventOut)
def update_existing_event(event_id: int, event: EventUpdate, db: Session = Depends(get_db)):
    return update_event(db, event_id, event)

@router.delete("/{event_id}")
def delete_existing_event(event_id: int, db: Session = Depends(get_db)):
    result = delete_event(db, event_id)
    if not result:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    return {"detail": "Evento eliminado"}