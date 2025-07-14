from sqlalchemy.orm import Session
from models.ticket import Ticket
from schemas.ticket import TicketCreate

def create_ticket(db: Session, ticket: TicketCreate):
    db_ticket = Ticket(**ticket.dict())
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

def get_all_tickets(db: Session):
    return db.query(Ticket).all()

def get_ticket_by_id(db: Session, ticket_id: int):
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()

def update_ticket(db: Session, ticket_id: int, ticket: TicketCreate):
    db_ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if db_ticket:
        for field, value in ticket.dict().items():
            setattr(db_ticket, field, value)
        db.commit()
        db.refresh(db_ticket)
    return db_ticket

def delete_ticket(db: Session, ticket_id: int):
    db_ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if db_ticket:
        db.delete(db_ticket)
        db.commit()
    return {"detail": "Deleted successfully"}