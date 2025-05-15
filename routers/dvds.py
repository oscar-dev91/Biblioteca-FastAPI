from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import dvd as schemas
from services import dvd as services
from deps import get_db

router = APIRouter(prefix="/dvds", tags=["DVDs"])

@router.get('/', response_model=list[schemas.DVDOut])
def listar(db: Session = Depends(get_db)):
    """# ``GET /dvds/`` — Listar DVDs

Obtiene una lista de todos los DVDs registrados en el sistema.

## Respuesta
] ``200 OK``: Lista de DVDs registrados.

## Ejemplo de respuesta
```json
[
  {
    "id": 1,
    "duracion_minutos": 120,
    "clasificacion": "PG-13",
    "formato": "Blu-ray",
    "elemento": {
      "id": 3,
      "titulo": "La Era Digital",
      "autor": "Luis Martínez",
      "ano_publicacion": 2019,
      "tipo": "DVD"
    }
  }
]
```
    """
    return services.obtener_dvds

@router.get('/{dvd_id}', response_model=schemas.DVDOut)
def obtener_libro(libro_id: int, db: Session = Depends(get_db)):
    """# ``GET /dvds/{dvd_id}`` — Obtener DVD por ID

Recupera la información detallada de un DVD específico.

## Parámetros
* ``dvd_id (int)``: ID del DVD que se desea consultar.

## Respuesta
* ``200 OK``: DVD encontrado.
* ``404 Not Found``: Si no existe un DVD con el ID proporcionado.

## Ejemplo de respuesta
```json
{
  "id": 2,
  "duracion_minutos": 95,
  "clasificacion": "R",
  "formato": "DVD",
  "elemento": {
    "id": 4,
    "titulo": "Cine Negro",
    "autor": "Pedro González",
    "ano_publicacion": 2017,
    "tipo": "DVD"
  }
}
```
"""
    dvd = services.obtener_dvd(db, libro_id)
    if not dvd:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='DVD no encontrado')
    return dvd

@router.post('/', response_model=schemas.DVDOut)
def crear(dvd: schemas.DVDCreate, db: Session = Depends(get_db)):
    """# ``POST /dvds/`` — Crear DVD

Crea un nuevo DVD, registrando su información como elemento de biblioteca.

## Cuerpo de la solicitud
```json
{
  "titulo": "Mundos Paralelos",
  "autor": "Elena Ríos",
  "ano_publicacion": 2022,
  "duracion_minutos": 110,
  "clasificacion": "PG",
  "formato": "Blu-ray"
}
```
Respuesta
* ``201 Created``: DVD creado exitosamente.
    """
    return services.crear_dvd(db, dvd)

@router.put('/{dvd_id}', response_model=schemas.DVDOut)
def actualizar(dvd_id: int, dvd: schemas.DVDUpdate, db: Session = Depends(get_db)):
    """# ``PUT /dvds/{dvd_id}`` — Actualizar DVD

Actualiza la información de un DVD existente.

## Parámetros
* ``dvd_id``: ID del DVD a modificar.

Cuerpo de la solicitud
```json
{
  "duracion_minutos": 130
}
```
Respuesta
* ``200 OK``: DVD actualizado exitosamente.
* ``404 Not Found``: Si el DVD no existe.
    """
    dvd_actualizado = services.actualizar_dvd(db, dvd_id, dvd)
    if not dvd_actualizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='DVD no encontrado')
    return dvd_actualizado

@router.delete('/{dvd_id}', status_code=status.HTTP_204_NO_CONTENT)
def eliminar(dvd_id: int, db: Session = Depends(get_db)):
    """# ``DELETE /dvds/{dvd_id}`` — Eliminar DVD

Elimina un DVD del sistema junto con su entrada asociada.

## Parámetros
* ``dvd_id``: ID del DVD a eliminar.

## Respuesta
* ``204 No Content``: Eliminación exitosa.
* ``404 Not Found``: Si el DVD no existe.
    """
    eliminado = services.eliminar_dvd(db, dvd_id)
    if not eliminado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='DVD no encontrado')
    return