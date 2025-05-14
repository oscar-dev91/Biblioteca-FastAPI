from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class ElementoBiblioteca(Base):
    __tablename__ = "ElementoBiblioteca"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), nullable=False)
    autor = Column(String(255), nullable=False)
    ano_publicacion = Column(Integer, nullable=False)
    tipo = Column(String(50), nullable=False)