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

app = FastAPI()

# Registra los exception handlers
app.add_exception_handler(StarletteHTTPException, custom_http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)

# Incluye las rutas
app.include_router(ritual_api_app)