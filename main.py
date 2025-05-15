from fastapi import FastAPI
from routers import libros, revistas, dvds

app = FastAPI()

app.include_router(libros.router)
app.include_router(revistas.router)
app.include_router(dvds.router)