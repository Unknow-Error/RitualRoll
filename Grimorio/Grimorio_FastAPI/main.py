import sys
import os

# Obtén el directorio raíz del proyecto (uno nivel arriba del directorio actual)
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Agrega el directorio raíz al sys.path para poder importar módulos y paquetes desde ahí
sys.path.append(root_dir)

from fastapi import FastAPI
from RitualAPI.ritualAPI import app as ritual_api_app

# Crea una nueva instancia de FastAPI si necesitas agregar más rutas globales o middleware
app = FastAPI()

# Aquí puedes agregar middleware global, configuraciones adicionales, etc.
# app.add_middleware(...)

# Incluye las rutas definidas en ritualAPI.py
app.include_router(ritual_api_app)