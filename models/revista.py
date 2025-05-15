from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from .elemento import ElementoBiblioteca

class Revista(Base):
    """ Representa una revista dentro de la base de datos como una extensión del modelo ElementoBiblioteca.

    Esta clase hereda de `Base` y define una tabla 'Revista' con campos específicos 
    relacionados con publicaciones periódicas, incluyendo el número de edición y la categoría.

    Atributos:
    * `id (int)`: Identificador único de la revista, enlazado a ElementoBiblioteca mediante clave foránea.
    * `numero_edicion (int)`: Número de edición de la revista.
    * `categoria (str)`: Categoría de la revista (ej. ciencia, moda, tecnología).
    * `elemento (ElementoBiblioteca)`: Relación uno a uno con el modelo ElementoBiblioteca.
    """
    __tablename__ = 'Revista'
    
    id = Column(Integer, ForeignKey('ElementoBiblioteca.id', ondelete='CASCADE'), primary_key=True, index=True)
    numero_edicion = Column(Integer, nullable=False)
    categoria = Column(String(50), nullable=False, index=True)
    
    elemento = relationship('ElementoBiblioteca', backref='revista', uselist=False)