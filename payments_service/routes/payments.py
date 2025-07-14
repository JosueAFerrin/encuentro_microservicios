from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import PaymentCreate, PaymentOut
from services import payment_service
from db.database import get_db

router = APIRouter()

@router.post("/", response_model=PaymentOut)
def create_new_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    return payment_service.create_payment(db, payment)

@router.get("/", response_model=list[PaymentOut])
def list_payments(db: Session = Depends(get_db)):
    return payment_service.get_all_payments(db)

@router.get("/{payment_id}", response_model=PaymentOut)
def get_payment(payment_id: int, db: Session = Depends(get_db)):
    return payment_service.get_payment_by_id(db, payment_id)

@router.put("/{payment_id}", response_model=PaymentOut)
def update_payment(payment_id: int, payment: PaymentCreate, db: Session = Depends(get_db)):
    return payment_service.update_payment(db, payment_id, payment)

@router.delete("/{payment_id}")
def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    return payment_service.delete_payment(db, payment_id)
