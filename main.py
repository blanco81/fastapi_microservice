from fastapi import FastAPI
from routers import category, product
from config.database import Base, engine

app = FastAPI()

app.include_router(category.router, prefix="/api/v1")
app.include_router(product.router, prefix="/api/v1")


@app.on_event("startup")
async def startup():
    # Crear la base de datos si no existe
    Base.metadata.create_all(bind=engine)

    # Otros pasos de inicialización si los necesitas
    print("La aplicación se ha iniciado y la base de datos está lista.")
