from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import revista as schemas
from services import revista as services
from deps import get_db

router = APIRouter(prefix='/revistas', tags=['Revistas'])

@router.get('/', response_model=list[schemas.RevistaOut])
def listar(db: Session = Depends(get_db)):
    """# ``GET /revistas/`` — Listar revistas

Obtiene una lista de todas las revistas registradas en el sistema.

## Respuesta
* ``200 OK``: Lista de revistas registradas.

## Ejemplo de respuesta
```json
[
  {
    "id": 1,
    "numero": 45,
    "mes_publicacion": "Mayo",
    "periodicidad": "Mensual",
    "elemento": {
      "id": 5,
      "titulo": "Ciencia Hoy",
      "autor": "Varios",
      "ano_publicacion": 2023,
      "tipo": "Revista"
    }
  }
]
```   
    """
    return services.obtener_revistas(db)

@router.get('/{revista_id}', response_model=schemas.RevistaOut)
def obtener_revista(revista_id: int, db: Session = Depends(get_db)):
    """# ``GET /revistas/{revista_id}`` — Obtener revista por ID

Recupera la información detallada de una revista específica.

## Parámetros
* ``revista_id``: ID de la revista a consultar.

## Respuesta
* ``200 OK``: Revista encontrada.
* ``404 Not Found``: Si no existe una revista con ese ID.
    """
    revista = services.obtener_revista(db, revista_id)
    if not revista:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Revista no encontrada')
    return revista

@router.post('/', response_model=schemas.RevistaOut)
def crear(revista: schemas.RevistaCreate, db: Session = Depends(get_db)):
    """# ``POST /revistas/`` — Crear revista

Crea una nueva revista como elemento del sistema.

## Cuerpo de la solicitud
```json
{
  "titulo": "Innovación Empresarial",
  "autor": "Redacción Innovar",
  "ano_publicacion": 2023,
  "numero": 12,
  "mes_publicacion": "Abril",
  "periodicidad": "Trimestral"
}
```
## Respuesta
* ``201 Created``: Revista creada exitosamente.
    """
    return services.crear_revista(db, revista)

@router.put('/{revista_id}', response_model=schemas.RevistaOut)
def actualizar(revista_id: int, revista: schemas.RevistaUpdate, db: Session = Depends(get_db)):
    """# ``PUT /revistas/{revista_id}`` — Actualizar revista

Actualiza la información de una revista existente.

## Parámetros
* ``revista_id``: ID de la revista.

## Cuerpo de la solicitud
```json
{
  "numero": 13,
  "mes_publicacion": "Junio"
}
```
## Respuesta
* ``200 OK``: Revista actualizada.
* ``404 Not Found``: Revista no encontrada.
    """
    revista_actualizada = services.actualizar_revista(db, revista_id, revista)
    if not revista_actualizada:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Revista no encontrada')
    return revista_actualizada

@router.delete('/{revista_id}', status_code=status.HTTP_204_NO_CONTENT)
def eliminar(revista_id: int, db: Session = Depends(get_db)):
    """# ``DELETE /revistas/{revista_id}`` — Eliminar revista

Elimina una revista del sistema.

## Parámetros
* ``revista_id``: ID de la revista.

## Respuesta
* ``204 No Content``: Revista eliminada.
* ``404 Not Found``: Si no existe.
    """
    eliminado = services.eliminar_revista(db, revista_id)
    if not eliminado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Revista no encontrada')
    return