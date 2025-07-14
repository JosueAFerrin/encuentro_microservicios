from pydantic import BaseModel

class LocationBase(BaseModel):
    nombre: str
    capacidad: int
    precio: float

class LocationCreate(LocationBase):
    pass

class LocationUpdate(LocationBase):
    pass

class LocationOut(LocationBase):
    id: int

    class Config:
        orm_mode = True