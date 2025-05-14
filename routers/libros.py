from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import libro as schemas
from services import libro as services
from deps import get_db

router = APIRouter(prefix="/libros", tags=["Libros"])

@router.get("/", response_model=list[schemas.LibroOut])
def listar(db: Session = Depends(get_db)):
    """# 📚 ``GET /libros/`` — Listar libros

Obtiene una lista de todos los libros registrados en el sistema.
## Respuesta
* 200 OK: Lista de libros registrados.

## Ejemplo de respuesta
```json
[
  {
    "id": 1,
    "isbn": "9781234567890",
    "numero_paginas": 320,
    "genero": "Ciencia Ficción",
    "editorial": "Nova Editores",
    "elemento": {
      "id": 1,
      "titulo": "El Viaje Estelar",
      "autor": "Ana Pérez",
      "ano_publicacion": 2020,
      "tipo": "Libro"
    }
  }
]
```
    """
    return services.obtener_libros(db)

@router.get("/{libro_id}", response_model=schemas.LibroOut)
def obtener_libro(libro_id: int, db: Session = Depends(get_db)):
    """# 🔍 ``GET /libros/{libro_id}`` — Obtener libro por ID

Recupera la información detallada de un libro específico, incluyendo los datos del elemento de biblioteca relacionado.
## Parámetros
* ``libro_id`` (int): ID del libro que se desea consultar.

Respuesta
* ``200 OK``: Libro encontrado.
* ``404 Not Found``: Si no existe un libro con el ID proporcionado.

## Ejemplo de respuesta
```json
{
  "id": 2,
  "isbn": "9788491234567",
  "numero_paginas": 198,
  "genero": "Novela",
  "editorial": "Letras del Sur",
  "elemento": {
    "id": 2,
    "titulo": "Historias del Sur",
    "autor": "Gabriela Torres",
    "ano_publicacion": 2018,
    "tipo": "Libro"
  }
}
```
    """
    libro = services.obtener_libro(db, libro_id)
    if not libro: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Libro no encontrado")
    return libro

@router.post("/", response_model=schemas.LibroOut)
def crear(libro: schemas.LibroCreate, db: Session = Depends(get_db)):
    """# 📝 ``POST /libros/`` — Crear libro

Crea un nuevo libro, registrando primero su información como elemento de biblioteca.
## Cuerpo de la solicitud

* `titulo`: Título del libro
* `autor`: Autor del libro
* `ano_publicacion`: Año de publicación
* `isbn`: Código ISBN único
* `numero_paginas`: Cantidad de páginas
* `genero`: Género literario
* `editorial`: Nombre de la editorial

## Ejemplo de solicitud
```json
{
  "titulo": "Inteligencia Artificial Moderna",
  "autor": "Carlos Gómez",
  "ano_publicacion": 2021,
  "isbn": "9789876543210",
  "numero_paginas": 250,
  "genero": "Tecnología",
  "editorial": "TechBooks"
}
```

## Respuesta
* ``201 Created``: Libro creado exitosamente.
    """
    return services.crear_libro(db, libro)

@router.put("/{libro_id}", response_model=schemas.LibroOut)
def actualizar(libro_id: int, libro: schemas.LibroUpdate, db: Session = Depends(get_db)):
    """# ✏️ ``PUT /libros/{libro_id}`` — Actualizar libro

Actualiza la información de un libro existente.
## Parámetros
* ``libro_id``: ID del libro a modificar.

## Cuerpo de la solicitud

Se pueden incluir uno o varios de los siguientes campos:

    ``titulo``, ``autor``, ``ano_publicacion``, ``isbn``, ``numero_paginas``, ``genero``, ``editorial``

## Ejemplo de solicitud
```json
{
  "titulo": "IA y Robótica",
  "numero_paginas": 300
}
```
## Respuesta
* ``200 OK``: Libro actualizado exitosamente.
* ``404 Not Found``: Si el libro no existe.
    """
    libro_actualizado = services.actualizar_libro(db, libro_id, libro)
    if not libro_actualizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Libro no encontrado")
    return libro_actualizado

@router.delete("/{libro_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar(libro_id: int, db: Session = Depends(get_db)):
    """# 🗑️ ``DELETE /libros/{libro_id}`` — Eliminar libro

Elimina un libro del sistema, junto con su entrada asociada en la tabla de elementos de biblioteca.
## Parámetros
* `libro_id`: ID del libro a eliminar.

## Respuesta
* ``204 No Content``: Eliminación exitosa.
* ``404 Not Found``: Si el libro no existe.
    """
    eliminado = services.eliminar_libro(db, libro_id)
    if not eliminado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Libro no encontrado")
    return 