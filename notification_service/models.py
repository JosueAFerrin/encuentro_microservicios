from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from db.database import Base

class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, index=True)
    destinatario = Column(String, nullable=False)
    asunto = Column(String, nullable=False)
    mensaje = Column(String, nullable=False)
    estado = Column(String, default="pendiente")  # pendiente, enviado, fallido
    fecha_envio = Column(DateTime, default=datetime.utcnow)