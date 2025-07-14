from sqlalchemy.orm import Session
from models import Purchase
from schemas.purchase import PurchaseCreate

def get_all_purchases(db: Session):
    return db.query(Purchase).all()

def get_purchase_by_id(db: Session, purchase_id: int):
    return db.query(Purchase).filter(Purchase.id == purchase_id).first()

def create_purchase(db: Session, purchase: PurchaseCreate):
    db_purchase = Purchase(**purchase.dict())
    db.add(db_purchase)
    db.commit()
    db.refresh(db_purchase)
    return db_purchase

def delete_purchase(db: Session, purchase_id: int):
    db_purchase = get_purchase_by_id(db, purchase_id)
    if db_purchase:
        db.delete(db_purchase)
        db.commit()
    return db_purchase