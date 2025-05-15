from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from .elemento import ElementoBiblioteca

class DVD(Base):
    """ Representa un DVD dentro de la base de datos como una extensión del modelo ElementoBiblioteca.

    Esta clase hereda de `Base` y define una tabla 'DVD' con campos específicos 
    relacionados con los discos digitales, incluyendo duración y género.

    Atributos:
    * `id (int)`: Identificador único del DVD, enlazado a ElementoBiblioteca mediante clave foránea.
    * `duracion (int)`: Duración del contenido del DVD en minutos.
    * `genero (str)`: Género del contenido del DVD (ej. documental, acción, comedia).
    * `elemento (ElementoBiblioteca)`: Relación uno a uno con el modelo ElementoBiblioteca.
    """
    __tablename__ = "DVD"
    
    id = Column(Integer, ForeignKey("ElementoBiblioteca.id", ondelete='CASCADE'), primary_key=True, index=True)
    duracion = Column(Integer, nullable=False)
    genero = Column(String(50), nullable=False, index=True)
    
    elemento = relationship("ElementoBiblioteca", backref='dvd', uselist=False)