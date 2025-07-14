from sqlalchemy.orm import Session
from models import Payment
from schemas import PaymentCreate

def create_payment(db: Session, payment: PaymentCreate):
    db_payment = Payment(**payment.dict())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def get_all_payments(db: Session):
    return db.query(Payment).all()

def get_payment_by_id(db: Session, payment_id: int):
    return db.query(Payment).filter(Payment.id == payment_id).first()

def update_payment(db: Session, payment_id: int, payment_data: PaymentCreate):
    db_payment = get_payment_by_id(db, payment_id)
    if db_payment:
        for key, value in payment_data.dict().items():
            setattr(db_payment, key, value)
        db.commit()
        db.refresh(db_payment)
    return db_payment

def delete_payment(db: Session, payment_id: int):
    db_payment = get_payment_by_id(db, payment_id)
    if db_payment:
        db.delete(db_payment)
        db.commit()
    return db_payment
