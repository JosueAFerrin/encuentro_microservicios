from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.ticket import TicketCreate, TicketOut
from db.database import SessionLocal
from services.ticket_service import (
    create_ticket, get_all_tickets, get_ticket_by_id, update_ticket, delete_ticket
)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=TicketOut)
def create_new_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    return create_ticket(db, ticket)

@router.get("/", response_model=list[TicketOut])
def read_tickets(db: Session = Depends(get_db)):
    return get_all_tickets(db)

@router.get("/{ticket_id}", response_model=TicketOut)
def read_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = get_ticket_by_id(db, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

@router.put("/{ticket_id}", response_model=TicketOut)
def update_ticket_data(ticket_id: int, ticket: TicketCreate, db: Session = Depends(get_db)):
    return update_ticket(db, ticket_id, ticket)

@router.delete("/{ticket_id}")
def remove_ticket(ticket_id: int, db: Session = Depends(get_db)):
    return delete_ticket(db, ticket_id)