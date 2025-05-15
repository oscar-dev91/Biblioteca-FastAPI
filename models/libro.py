from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from .elemento import ElementoBiblioteca

class Libro(Base):
    """ Representa un libro dentro de la base de datos como una extensión del modelo ElementoBiblioteca.

    Esta clase hereda de `Base` y define una tabla 'Libro' con campos específicos 
    relacionados con los libros físicos, incluyendo el ISBN, número de páginas, género y editorial.

    Atributos:
    * `id (int)`: Identificador único del libro, enlazado a ElementoBiblioteca mediante clave foránea.
    * `isbn (str)`: Código ISBN único del libro.
    * `numero_paginas (int)`: Número total de páginas del libro.
    * `genero (str)`: Género literario del libro (ej. ficción, historia, ciencia).
    * `editorial (str)`: Nombre de la editorial responsable de la publicación del libro.
    * `elemento (ElementoBiblioteca)`: Relación uno a uno con el modelo ElementoBiblioteca.
    """
    __tablename__ = "Libro"

    id = Column(Integer, ForeignKey("ElementoBiblioteca.id", ondelete='CASCADE'), primary_key=True, index=True)
    isbn = Column(String(50), unique=True, index=True)
    numero_paginas = Column(Integer, nullable=False)
    genero = Column(String(100), index=True)
    editorial = Column(String(255), nullable=False, index=True)

    elemento = relationship("ElementoBiblioteca", backref='libro', uselist=False)