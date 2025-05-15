from pydantic import BaseModel
from typing import Optional
from .elemento import ElementoOut

class RevistaBase(BaseModel):
    """
    Modelo base para representar la información común de una revista.

    Atributos:
    * numero_edicion (int): Número de edición de la revista.
    * categoria (str): Categoría temática de la revista (ej. ciencia, moda, tecnología).
    """
    numero_edicion: int
    categoria: str
    
    class Config:
        from_attributes = True
        
class RevistaCreate(RevistaBase):
    """
    Modelo para la creación de una nueva revista, extiende RevistaBase.

    Atributos adicionales:
    * titulo (str): Título de la revista.
    * autor (str): Nombre del autor o editor responsable.
    * ano_publicacion (int): Año de publicación de la revista.
    """
    titulo: str
    autor: str
    ano_publicacion: int
    
class RevistaUpdate(BaseModel):
    """
    Modelo para la actualización parcial de los datos de una revista.

    Todos los campos son opcionales para permitir actualizaciones parciales.

    Atributos:
    * titulo (Optional[str]): Título de la revista.
    * autor (Optional[str]): Autor o editor responsable.
    * ano_publicacion (Optional[int]): Año de publicación de la revista.
    * numero_edicion (Optional[int]): Número de edición.
    * categoria (Optional[str]): Categoría temática.
    """
    titulo: Optional[str]
    autor: Optional[str]
    ano_publicacion: Optional[int]
    numero_edicion: Optional[int]
    categoria: Optional[str]
    
class RevistaOut(RevistaBase):
    """
    Modelo de salida que representa una revista con información adicional.

    Atributos:
    * id (int): Identificador único de la revista.
    * elemento (ElementoOut): Información relacionada del modelo ElementoBiblioteca.
    """
    id:int
    elemento: ElementoOut
    
    class Config:
        from_attributes = True