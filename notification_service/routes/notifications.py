from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal
from schemas.notification import NotificationCreate, NotificationOut
from services.notification_service import (
    get_all_notifications, get_notification_by_id,
    create_notification, delete_notification
)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[NotificationOut])
def list_notifications(db: Session = Depends(get_db)):
    return get_all_notifications(db)

@router.get("/{notification_id}", response_model=NotificationOut)
def get_notification(notification_id: int, db: Session = Depends(get_db)):
    notif = get_notification_by_id(db, notification_id)
    if not notif:
        raise HTTPException(status_code=404, detail="Notificación no encontrada")
    return notif

@router.post("/", response_model=NotificationOut)
def create_new_notification(notif: NotificationCreate, db: Session = Depends(get_db)):
    return create_notification(db, notif)

@router.delete("/{notification_id}")
def delete_existing_notification(notification_id: int, db: Session = Depends(get_db)):
    result = delete_notification(db, notification_id)
    if not result:
        raise HTTPException(status_code=404, detail="Notificación no encontrada")
    return {"detail": "Notificación eliminada"}