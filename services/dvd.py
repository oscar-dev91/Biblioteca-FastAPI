from sqlalchemy.orm import Session, joinedload
from models.dvd import DVD
from models.elemento import ElementoBiblioteca
from schemas import dvd as Schema

def crear_dvd(db: Session, dvd: Schema.DVDCreate):
    """Crea un Elemento Biblioteca y luego un DVD respetando la herencia

    Args:
        db (Session): Sesión de la base de datos
        dvd (Schema.DVDCreate): Valores del DVD a crear en la base de datos

    Returns:
        DVD: DVD registrado en la base de datos
    """
    elemento = ElementoBiblioteca(
        titulo = dvd.titulo,
        autor = dvd.autor,
        ano_publicacion = dvd.ano_publicacion,
        tipo = 'DVD'
    )
    db.add(elemento)
    db.flush()
    
    dvd_db = DVD(
        id = elemento.id,
        duracion = dvd.duracion,
        genero = dvd.genero
    )
    db.add(dvd_db)
    db.commit()
    db.refresh(dvd_db)
    return dvd_db

def obtener_dvds(db: Session):
    """Función para obtener todos los DVDs de la base de datos

    Args:
        db (Session): Sesión de la base de datos

    Returns:
        List: Lista de todos los DVDs
    """
    return db.query(DVD).options(joinedload(DVD.elemento)).all()

def obtener_dvd(db: Session, dvd_id: int):
    """Obtiene un DVD por su ID

    Args:
        db (Session): Sesión de la base de datos
        dvd_id (int): ID del DVD que se desea obtener

    Returns:
        DVD: DVD correspondiente al ID, si existe
    """
    return db.query(DVD).options(joinedload(DVD.elemento)).filter(DVD.id == dvd_id).first()

def actualizar_dvd(db: Session, dvd_id: int, datos: Schema.DVDUpdate):
    """Actualiza la información de un DVD y su elemento asociado en la base de datos

    Args:
        db (Session): Sesión de la base de datos
        dvd_id (int): ID del DVD que se desea actualizar
        datos (Schema.DVDUpdate): Datos actualizados para el DVD

    Returns:
        DVD | None: DVD actualizado si existe, de lo contrario None
    """
    dvd = db.query(DVD).filter(DVD.id == dvd_id).first()
    if not dvd:
        return None
    
    elemento = db.query(ElementoBiblioteca).filter(ElementoBiblioteca.id == dvd_id).first()
    if not elemento:
        return None
    
    # Actualizar campos en Elemento Biblioteca
    if datos.titulo is not None:
        elemento.titulo = datos.titulo
    if datos.autor is not None:
        elemento.autor = datos.autor
    if datos.ano_publicacion is not None:
        elemento.ano_publicacion = datos.ano_publicacion
    
    # Actualizar campos en DVD
    if datos.duracion is not None:
        dvd.duracion = datos.duracion
    if datos.genero is not None:
        dvd.genero = datos.genero

    db.commit()
    db.refresh(dvd)
    return dvd

def eliminar_dvd(db: Session, dvd_id: int):
    """Elimina un DVD y su elemento asociado de la base de datos

    Args:
        db (Session): Sesión de la base de datos
        dvd_id (int): ID del DVD que se desea eliminar

    Returns:
        bool: True si se eliminó correctamente, False si no se encontró el DVD
    """
    dvd = db.query(DVD).filter(DVD.id == dvd_id).first()
    
    if not dvd:
        return False
    
    elemento = db.query(ElementoBiblioteca).filter(ElementoBiblioteca.id == dvd.id).first()
    if elemento:
        db.delete(dvd)
        db.delete(elemento)
        db.commit()
        return True
    return False