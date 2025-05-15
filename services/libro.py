from sqlalchemy.orm import Session, joinedload
from models.libro import Libro
from models.elemento import ElementoBiblioteca
from schemas import libro as Schema

def crear_libro(db: Session, libro: Schema.LibroCreate):
    """Crea un Elemento Biblioteca y luego Libro respetando la herencia

    Args:
        db (Session): Sesión de la base de datos
        libro (Schema.LibroCreate): Valores del libro a crear en la base de datos

    Returns:
        Libro: Libro registrado en la base de datos
    """
    elemento = ElementoBiblioteca(
        titulo = libro.titulo,
        autor = libro.autor,
        ano_publicacion = libro.ano_publicacion,
        tipo= 'Libro'
    )
    db.add(elemento)
    db.flush() # Para obtener el ID antes de hacer commit
    
    libro_db = Libro(
        id = elemento.id,
        isbn = libro.isbn,
        numero_paginas = libro.numero_paginas,
        genero = libro.genero,
        editorial = libro.editorial
    )
    db.add(libro_db)
    db.commit()
    db.refresh(libro_db)
    return libro_db

def obtener_libros(db: Session):
    """Función para obtener todos los libros de la Base de datos

    Args:
        db (Session): Sesión de la base de datos

    Returns:
        List: Lista de todos los libros
    """
    return db.query(Libro).options(joinedload(Libro.elemento)).all()

def obtener_libro(db: Session, libro_id: int):
    """Obtener libro por ID

    Args:
        db (Session): Sesión de la base de datos
        libro_id (int): _description_

    Returns:
        Libro: Libro por ID
    """
    return db.query(Libro).options(joinedload(Libro.elemento)).filter(Libro.id == libro_id).first()

def actualizar_libro(db: Session, libro_id: int, datos: Schema.LibroUpdate):
    """Actualiza la información de un libro y su elemento asociado en la base de datos

    Args:
    * db (Session): Sesión de la base de datos
    * libro_id (int): ID del libro que se desea actualizar
    * datos (Schema.LibroUpdate): Datos actualizados para el libro

    Returns:
    * Libro | None: Libro actualizado si existe, de lo contrario None
    """
    libro = db.query(Libro).filter(Libro.id == libro_id).first()
    if not libro:
        return None
    
    elemento = db.query(ElementoBiblioteca).filter(ElementoBiblioteca.id == libro_id).first()
    if not elemento:
        return None
    
    # Actualizar campos en ElementoBiblioteca
    if datos.titulo is not None:
        elemento.titulo = datos.titulo
    if datos.autor is not None:
        elemento.autor = datos.autor
    if datos.ano_publicacion is not None:
        elemento.ano_publicacion = datos.ano_publicacion
        
    # Actualizar campos en Libro
    if datos.isbn is not None:
        libro.isbn = datos.isbn
    if datos.numero_paginas is not None:
        libro.numero_paginas = datos.numero_paginas
    if datos.genero is not None:
        libro.genero = datos.genero
    if datos.editorial is not None:
        libro.editorial = datos.editorial
        
    db.commit()
    db.refresh(libro)
    return libro

def eliminar_libro(db: Session, libro_id: int):
    """Elimina un libro y su elemento asociado de la base de datos

    Args:
        db (Session): Sesión de la base de datos
        libro_id (int): ID del libro que se desea eliminar

    Returns:
        bool: True si se eliminó correctamente, False si no se encontró el libro
    """
    libro = db.query(Libro).filter(Libro.id == libro_id).first()
    if not libro:
        return False

    elemento = db.query(ElementoBiblioteca).filter(ElementoBiblioteca.id == libro_id).first()
    if elemento:
        db.delete(libro)
        db.delete(elemento)
        db.commit()
        return True
    return False
