from pydantic import BaseModel
from typing import Optional

class ElementoBase(BaseModel):
    titulo: str
    autor: str
    ano_publicacion: int
    tipo: str

    class Config:
        from_attributes = True

class ElementoCreate(ElementoBase):
    pass

class ElementoUpdate(BaseModel):
    titulo: Optional[str]
    autor: Optional[str]
    ano_publicacion: Optional[int]
    tipo: Optional[str]

class ElementoOut(ElementoBase):
    id: int

    class Config:
        from_attributes = True
