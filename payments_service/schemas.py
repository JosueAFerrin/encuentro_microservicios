from pydantic import BaseModel
from datetime import datetime

class PaymentBase(BaseModel):
    monto: float
    metodo_pago: str
    estado: str = "pendiente"
    usuario_id: int

class PaymentCreate(PaymentBase):
    pass

class PaymentOut(PaymentBase):
    id: int
    fecha_pago: datetime

    class Config:
        from_attributes = True
