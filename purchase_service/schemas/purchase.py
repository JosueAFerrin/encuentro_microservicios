from pydantic import BaseModel
from datetime import datetime

class PurchaseBase(BaseModel):
    user_id: int
    event_id: int
    cantidad: int

class PurchaseCreate(PurchaseBase):
    pass

class PurchaseOut(PurchaseBase):
    id: int
    fecha_compra: datetime

    class Config:
        orm_mode = True