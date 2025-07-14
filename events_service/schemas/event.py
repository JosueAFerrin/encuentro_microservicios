from pydantic import BaseModel
from datetime import datetime

class EventBase(BaseModel):
    nombre: str
    descripcion: str
    fecha_inicio: datetime
    fecha_fin: datetime
    lugar: str
    organizador_id: int

class EventCreate(EventBase):
    pass

class EventUpdate(EventBase):
    pass

class EventOut(EventBase):
    id: int

    class Config:
        orm_mode = True