from fastapi import FastAPI
from routers import libros

app = FastAPI()

app.include_router(libros.router)