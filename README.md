# 📚 API Biblioteca

Este proyecto es una API RESTful construida con FastAPI para gestionar una biblioteca. Maneja distintos tipos de elementos bibliográficos: libros, DVDs y revistas, todos heredando de un modelo base llamado ElementoBiblioteca.

## 🚀 Tecnologías utilizadas

* FastAPI
* SQLAlchemy
* MySQL
* Pydantic
* Uvicorn
* Python 3.11+

## ⚙️ Instalación y configuración
1. Clonar el repositorio
````bash
git clone https://github.com/tu-usuario/Biblioteca-FastAPI.git
cd biblioteca-api
````
2. Crear entorno virtual
````bash
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
````
3. Instalar dependencias
````bash
pip install -r requirements.txt
````
4. Variables de entorno

El archivo .env debe contener las credenciales de conexión a la base de datos. Ejemplo:
````bash
DB_HOST=localhost
DB_PORT=3306
DB_USER=usuario
DB_PASSWORD=contraseña
DB_NAME=biblioteca
````
## 🗂️ Estructura del proyecto
````bash
app/
├── main.py                   # Punto de entrada de la aplicación
├── database.py               # Configuración de la base de datos
├── models/
│   ├── elemento.py           # Modelo base ElementoBiblioteca
│   ├── libro.py              # Modelo para libros
│   ├── dvd.py                # Modelo para DVDs
│   └── revista.py            # Modelo para revistas
├── routers/
│   ├── libros.py             # Rutas relacionadas con libros
│   ├── dvds.py               # Rutas relacionadas con DVDs
│   └── revistas.py           # Rutas relacionadas con revistas
├── services/
│   ├── elemento.py           # Lógica de negocio para el modelo base
│   ├── libro.py              # Lógica de negocio para libros
│   ├── dvd.py                # Lógica de negocio para DVDs
│   └── revista.py            # Lógica de negocio para revistas
├── schemas/
│   ├── libro.py              # Esquemas Pydantic para libros
│   ├── dvd.py                # Esquemas Pydantic para DVDs
│   └── revista.py            # Esquemas Pydantic para revistas
└── exceptions.py             # Manejo de errores personalizados
````
## 🧱 Estructura de la base de datos

La base de datos está compuesta por las siguientes tablas:

* ``ElementoBiblioteca``: tabla base con campos comunes
* ``Libro``: hereda de ``ElementoBiblioteca`` (con ISBN, editorial, etc.)
* ``DVD``: hereda de ``ElementoBiblioteca`` (con duración y género)
* ``Revista``: hereda de ``ElementoBiblioteca`` (con edición y categoría)

## ▶️ Ejecutar el servidor
````bash
uvicorn app.main:app --reload
````
Accede a la documentación interactiva en:
* Swagger UI: http://localhost:8000/docs
* ReDoc: http://localhost:8000/redoc