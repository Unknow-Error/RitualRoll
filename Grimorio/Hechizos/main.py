import sys
import os

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

# Configura sys.path para importar correctamente
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_dir)

# Importa router y los handlers
from RitualAPI.ritualAPI import router as ritual_api_app
from RitualAPI.ritualError import (
    custom_http_exception_handler,
    validation_exception_handler,
    global_exception_handler
)

from BaseCondenados.cripta import router as cripta_router
from BaseCondenados.baseDatos import crear_db_y_tablas

app = FastAPI(
    title="RitualRoll API",
    description="API para mecánicas de dados, personajes y gestión de usuarios.",
    version="0.1.0",
)

@app.on_event("startup")
def on_startup():
    """
        Función que se ejecuta al iniciar la aplicación.
        Crea las tablas de la base de datos si no existen.
    """
    print("Iniciando la aplicación FastAPI...")
    crear_db_y_tablas()
    print("Tablas de la base de datos verificadas/creadas.")

# Registra los exception handlers
app.add_exception_handler(StarletteHTTPException, custom_http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)

# Rutas
app.include_router(cripta_router) 
app.include_router(ritual_api_app)

@app.get("/")
async def read_root():
    return {"message": "Bienvenido a RitualRoll API"}
