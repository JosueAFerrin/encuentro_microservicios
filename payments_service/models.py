from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from db.database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    monto = Column(Float, nullable=False)
    metodo_pago = Column(String, nullable=False)
    estado = Column(String, default="pendiente")
    fecha_pago = Column(DateTime(timezone=True), server_default=func.now())
    usuario_id = Column(Integer, nullable=True)  # Clave foránea no acoplada de momento
