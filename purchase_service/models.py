from sqlalchemy import Column, Integer, DateTime, ForeignKey
from datetime import datetime
from db.database import Base

class Purchase(Base):
    __tablename__ = "purchases"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    event_id = Column(Integer, nullable=False)
    cantidad = Column(Integer, nullable=False)
    fecha_compra = Column(DateTime, default=datetime.utcnow)