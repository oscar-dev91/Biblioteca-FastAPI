from sqlalchemy.orm import Session, joinedload
from models.revista import Revista
from models.elemento import ElementoBiblioteca
from schemas import revista as Schema

def crear_revista(db: Session, revista: Schema.RevistaCreate):
    """Crea un Elemento Biblioteca y luego una Revista respetando la herencia

    Args:
        db (Session): Sesión de la base de datos
        revista (Schema.RevistaCreate): Valores de la revista a crear en la base de datos

    Returns:
        Revista: Revista registrada en la base de datos
    """
    elemento = ElementoBiblioteca(
        titulo = revista.titulo,
        autor = revista.autor,
        ano_publicacion = revista.ano_publicacion,
        tipo = 'Revista'
    )
    db.add(elemento)
    db.flush()
    
    revista_db = Revista(
        id = elemento.id,
        numero_edicion = revista.numero_edicion,
        categoria = revista.categoria
    )
    db.add(revista_db)
    db.commit()
    db.refresh(revista_db)
    return revista_db

def obtener_revistas(db: Session):
    """Función para obtener todas las revistas de la base de datos

    Args:
        db (Session): Sesión de la base de datos

    Returns:
        List: Lista de todas las revistas
    """
    return db.query(Revista).options(joinedload(Revista.elemento)).all()

def obtener_revista(db: Session, revista_id: int):
    """Obtiene una revista por su ID

    Args:
        db (Session): Sesión de la base de datos
        revista_id (int): ID de la revista que se desea obtener

    Returns:
        Revista: Revista correspondiente al ID, si existe
    """
    return db.query(Revista).options(joinedload(Revista.elemento)).filter(Revista.id == revista_id).first()

def actualizar_revista(db: Session, revista_id: int, datos: Schema.RevistaUpdate):
    """Actualiza la información de una revista y su elemento asociado en la base de datos

    Args:
        db (Session): Sesión de la base de datos
        revista_id (int): ID de la revista que se desea actualizar
        datos (Schema.RevistaUpdate): Datos actualizados para la revista

    Returns:
        Revista | None: Revista actualizada si existe, de lo contrario None
    """
    revista = db.query(Revista).filter(Revista.id == revista_id).first()
    if not Revista:
        return None
    elemento = db.query(ElementoBiblioteca).filter(ElementoBiblioteca.id == revista_id).first()
    if not elemento:
        return None
    
    # Actualizar campos en ElementoBiblioteca
    if datos.titulo is not None:
        elemento.titulo = datos.titulo
    if datos.autor is not None:
        elemento.autor = datos.autor
    if datos.ano_publicacion is not None:
        elemento.ano_publicacion = datos.ano_publicacion
    
    # Actualizar campos en Revista
    if datos.numero_edicion is not None:
        revista.numero_edicion = datos.numero_edicion
    if datos.categoria is not None:
        revista.categoria = datos.categoria
        
    db.commit()
    db.refresh(revista)
    return revista

def eliminar_revista(db: Session, revista_id: int):
    """Elimina una revista y su elemento asociado de la base de datos

    Args:
        db (Session): Sesión de la base de datos
        revista_id (int): ID de la revista que se desea eliminar

    Returns:
        bool: True si se eliminó correctamente, False si no se encontró la revista
    """
    revista = db.query(Revista).filter(Revista.id == revista_id).first()
    if not revista:
        return False
    elemento = db.query(ElementoBiblioteca).filter(ElementoBiblioteca.id == revista_id).first()
    if elemento:
        db.delete(Revista)
        db.delete(elemento)
        db.commit()
        return True
    return False