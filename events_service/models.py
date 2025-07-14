from sqlalchemy import Column, Integer, String, DateTime
from db.database import Base

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String)
    fecha_inicio = Column(DateTime, nullable=False)
    fecha_fin = Column(DateTime, nullable=False)
    lugar = Column(String, nullable=False)
    organizador_id = Column(Integer, nullable=False)