from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cargar variables de entorno desde el archivo .env
load_dotenv()


# Obtener valores de las variables de entorno
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")
db_host = os.getenv("POSTGRES_HOST")
db_port = os.getenv("POSTGRES_PORT")

# Crear la URL de conexión a PostgreSQL
SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{db_host}:{db_port}/{db_name}"
#SQLALCHEMY_DATABASE_URL = "postgresql://kong:kongpass@localhost/loja"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
