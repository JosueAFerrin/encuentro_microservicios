from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal
from schemas.purchase import PurchaseCreate, PurchaseOut
from services.purchase_service import (
    get_all_purchases, get_purchase_by_id,
    create_purchase, delete_purchase
)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[PurchaseOut])
def list_purchases(db: Session = Depends(get_db)):
    return get_all_purchases(db)

@router.get("/{purchase_id}", response_model=PurchaseOut)
def get_purchase(purchase_id: int, db: Session = Depends(get_db)):
    purchase = get_purchase_by_id(db, purchase_id)
    if not purchase:
        raise HTTPException(status_code=404, detail="Compra no encontrada")
    return purchase

@router.post("/", response_model=PurchaseOut)
def create_new_purchase(purchase: PurchaseCreate, db: Session = Depends(get_db)):
    return create_purchase(db, purchase)

@router.delete("/{purchase_id}")
def delete_existing_purchase(purchase_id: int, db: Session = Depends(get_db)):
    result = delete_purchase(db, purchase_id)
    if not result:
        raise HTTPException(status_code=404, detail="Compra no encontrada")
    return {"detail": "Compra eliminada"}