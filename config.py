# app/config.py

from dotenv import load_dotenv
import os

load_dotenv()  # Carga el contenido del archivo .env

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# Para SQLAlchemy
DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Si usas una clave secreta
SECRET_KEY = os.getenv("SECRET_KEY")
