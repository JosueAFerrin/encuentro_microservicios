from sqlalchemy import Column, Integer, Float, String
from db.database import Base

class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    capacidad = Column(Integer, nullable=False)
    precio = Column(Float, nullable=False)