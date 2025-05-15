from pydantic import BaseModel
from typing import Optional
from .elemento import ElementoOut

class DVDBase(BaseModel):
    """
    Modelo base para representar la información común de un DVD.

    Atributos:
    * duracion (int): Duración del contenido del DVD en minutos.
    * genero (str): Género del DVD (ej. documental, acción, comedia).
    """
    duracion: int
    genero: str
    
    class Config:
        from_attributes = True
        
class DVDCreate(DVDBase):
    """
    Modelo para la creación de un nuevo DVD, extiende DVDBase.

    Atributos adicionales:
    * titulo (str): Título del DVD.
    * autor (str): Nombre del autor o director del DVD.
    * ano_publicacion (int): Año de publicación o lanzamiento del DVD.
    """
    titulo: str
    autor: str
    ano_publicacion: int
    
class DVDUpdate(BaseModel):
    """
    Modelo para la actualización parcial de los datos de un DVD.

    Todos los campos son opcionales para permitir actualizaciones parciales.

    Atributos:
    * titulo (Optional[str]): Título del DVD.
    * autor (Optional[str]): Autor o director del DVD.
    * ano_publicacion (Optional[int]): Año de publicación del DVD.
    * duracion (Optional[int]): Duración del contenido en minutos.
    * genero (Optional[str]): Género del DVD.
    """
    titulo: Optional[str]
    autor: Optional[str]
    ano_publicacion: Optional[int]
    duracion: Optional[int]
    genero: Optional[str]
    
class DVDOut(DVDBase):
    """
    Modelo de salida que representa un DVD con información adicional.

    Atributos:
    * id (int): Identificador único del DVD.
    * elemento (ElementoOut): Información relacionada del modelo ElementoBiblioteca.
    """
    id: int
    elemento: ElementoOut
    
    class Config:
        from_attributes = True