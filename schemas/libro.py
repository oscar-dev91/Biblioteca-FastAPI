from pydantic import BaseModel
from typing import Optional
from .elemento import ElementoOut

class LibroBase(BaseModel):
    """
    Modelo base para representar la información común de un libro.

    Atributos:
    * isbn (str): Código ISBN del libro.
    * numero_paginas (int): Número total de páginas del libro.
    * genero (str): Género literario del libro (ej. novela, ciencia ficción, etc.).
    * editorial (str): Nombre de la editorial que publicó el libro.
    """
    isbn: str
    numero_paginas: int
    genero: str
    editorial: str

    class Config:
        from_attributes = True

class LibroCreate(LibroBase):
    """
    Modelo para la creación de un nuevo libro, extiende LibroBase.

    Atributos adicionales:
    * titulo (str): Título del libro.
    * autor (str): Nombre del autor del libro.
    * ano_publicacion (int): Año de publicación del libro.
    """
    titulo: str
    autor: str
    ano_publicacion: int

class LibroUpdate(BaseModel):
    """
    Modelo para la actualización parcial de los datos de un libro.

    Todos los campos son opcionales para permitir actualizaciones parciales.

    Atributos:
    * titulo (Optional[str]): Título del libro.
    * autor (Optional[str]): Nombre del autor del libro.
    * ano_publicacion (Optional[int]): Año de publicación del libro.
    * isbn (Optional[str]): Código ISBN del libro.
    * numero_paginas (Optional[int]): Número de páginas del libro.
    * genero (Optional[str]): Género literario del libro.
    * editorial (Optional[str]): Editorial del libro.
    """
    titulo: Optional[str]
    autor: Optional[str]
    ano_publicacion: Optional[int]
    isbn: Optional[str]
    numero_paginas: Optional[int]
    genero: Optional[str]
    editorial: Optional[str]

class LibroOut(LibroBase):
    """
    Modelo de salida que representa un libro con información adicional.

    Atributos:
    * id (int): Identificador único del libro.
    * elemento (ElementoOut): Información relacionada del modelo ElementoBiblioteca.
    """
    id: int
    elemento: ElementoOut

    class Config:
        from_attributes = True
