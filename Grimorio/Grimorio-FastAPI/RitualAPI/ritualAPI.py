from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from ritualError import (
    custom_http_exception_handler,
    validation_exception_handler,
    global_exception_handler
)
import uuid
import sys
sys.path.append('/home/Nephelim/Documentos/Programacion/VSCodium-Projects/RitualRoll/Grimorio/Grimorio-FastAPI/Dados')
from dados import Dado
from mecanicaDados import Tirada_CWoD_20, TiradaMultiple



app = FastAPI()

# Handlers de error personalizados:
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi import Request

app.add_exception_handler(StarletteHTTPException, custom_http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)

# Almacenamiento temporal en memoria
tiradas_guardadas = {}

# Clase para realizar la petición POST
class TiradaEntrada_CWod_20(BaseModel):
    dados: int
    dificultad: Optional[int] = 6
    
class DadoNumericoEntrada(BaseModel):
    caras: int

class TiradaMultipleEntrada(BaseModel):
    dados: int
    caras: Optional[List[int]] = []
    dificultad: Optional[int] = 0
    bonus: Optional[int] = 0
    modoDificultad: Optional[bool] = True

# Para las Tiradas generales de cualquier mecanica:

@app.post("/RitualRoll/dadoNumerico/")
def crear_tirada_dado_num(input: DadoNumericoEntrada):
    if input.caras <= 0:
        raise HTTPException(status_code=422, detail="El dado debe tener al menos 1 cara.")
    
    tirada_id = str(uuid.uuid4())
    
    dado_obj = Dado(input.caras)
    
    tirada = dado_obj.tirar()
    tiradas_guardadas[tirada_id] = tirada
    
    return {
        "tirada_id": tirada_id,
        "resultado": tirada
    }

@app.post("/RitualRoll/tiradaMultiple/")
def crear_tirada_multiple(input: TiradaMultipleEntrada):    
    for cara in input.caras:
        if cara <= 0:
            raise HTTPException(status_code=422, detail="El dado debe tener al menos 1 cara.")   

    if not input.caras or len(input.caras) != input.dados:
        raise HTTPException(status_code=422, detail="Debes pasar una lista de caras del mismo largo que la cantidad de dados.")
    
    tirada_id = str(uuid.uuid4())

    dados_obj = [Dado(cara) for cara in input.caras]
    
    tirada = TiradaMultiple(
        dados=dados_obj,
        dificultad=input.dificultad,
        bonus=input.bonus,
        modo=input.modoDificultad
        )
    tiradas_guardadas[tirada_id] = tirada
    
    return {
        "tirada_id": tirada_id,
        "resultado": tirada.valoresJson
    }

# Para las Tiradas del Sistema CWod 20 :

@app.post("/RitualRoll/CWoD20/tirada/")
def crear_tirada_CWoD_20(input: TiradaEntrada_CWod_20):
    if input.dados <= 0:
        raise HTTPException(status_code=422, detail="Debe haber al menos un dado en la tirada.")
    
    tirada_id = str(uuid.uuid4())
    dados_obj = [Dado(10) for _ in range(input.dados)] # En WoD son todos 1D10.
    tirada = Tirada_CWoD_20(dados=dados_obj, dificultad=input.dificultad)

    tiradas_guardadas[tirada_id] = tirada
    
    return {
        "tirada_id": tirada_id,
        "resultado": tirada.resultadoTirada
    }

# Otra petición POST si aplica la regla de 10 en el resultado guardado de la tirada anterior.
@app.post("/RitualRoll/CWoD20/tirada/regla10/{tirada_id}")
def aplicar_regla_del_diez(tirada_id: str):
    tirada = tiradas_guardadas.get(tirada_id)

    if tirada is None:
        raise HTTPException(status_code=404, detail={"Tirada no encontrada"})

    try:
        nuevos_valores = tirada.tirada_regla_del_diez()
        tirada.evaluar_exitos() # Recalcula los éxitos incluyendo los nuevos dados
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al aplicar la Regla del 10: {str(e)}")

    return {
        "valores_sumados_por_regla10": nuevos_valores,
        "resultado_actualizado": tirada.resultadoTirada
    }


# Funcionalidades de las hojas de personaje WoD:
# GET : /hojasPersonaje/WoD/{juego}/{id} => Devuelve JSON del personaje
# POST: /hojasPersonaje/WoD/{juego}/crear_nueva_hoja => Crear nueva ficha
# PUT: /hojasPersonaje/WoD/{juego}/{id} => Actualizar hoja
# POST: /hojasPersonaje/WoD/{juego}/{id}/exportar/pdf => Genera plantilla en forma de pdf
# POST: /hojasPersonaje/WoD/{juego}/{id}/cargar/pdf => Carga pdf interactivo como JSON
# PUT: /hojasPersonaje/WoD/{juego}/{id}/cargar/pdf => Actualiza una plantilla segun el pdf.