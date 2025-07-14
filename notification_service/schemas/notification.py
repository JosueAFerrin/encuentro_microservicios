from pydantic import BaseModel
from datetime import datetime

class NotificationBase(BaseModel):
    destinatario: str
    asunto: str
    mensaje: str

class NotificationCreate(NotificationBase):
    pass

class NotificationOut(NotificationBase):
    id: int
    estado: str
    fecha_envio: datetime

    class Config:
        orm_mode = True