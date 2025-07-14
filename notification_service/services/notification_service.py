from sqlalchemy.orm import Session
from models import Notification
from schemas.notification import NotificationCreate
from datetime import datetime

def get_all_notifications(db: Session):
    return db.query(Notification).all()

def get_notification_by_id(db: Session, notification_id: int):
    return db.query(Notification).filter(Notification.id == notification_id).first()

def create_notification(db: Session, notif: NotificationCreate):
    db_notif = Notification(**notif.dict(), estado="pendiente", fecha_envio=datetime.utcnow())
    db.add(db_notif)
    db.commit()
    db.refresh(db_notif)
    return db_notif

def delete_notification(db: Session, notification_id: int):
    db_notif = get_notification_by_id(db, notification_id)
    if db_notif:
        db.delete(db_notif)
        db.commit()
    return db_notif