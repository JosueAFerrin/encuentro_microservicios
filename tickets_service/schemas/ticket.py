from pydantic import BaseModel

class TicketCreate(BaseModel):
    codigo: str
    estado: str

class TicketOut(TicketCreate):
    id: int

    class Config:
        from_attributes = True