from fastapi import FastAPI

app = FastAPI()

from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
from sistemaMecanicas import Tirada_CWoD_20
from dados import Dado
import uuid

# Almacenamiento temporal en memoria
tiradas_guardadas = {}

# Clase para realizar la petición POST
class TiradaEntrada_CWod_20(BaseModel):
    dados: int
    dificultad: Optional[int] = 6


@app.post("/tirada/wod20/")
def crear_tirada_CWoD_20(input: TiradaEntrada_CWod_20):
    tirada_id = str(uuid.uuid4())
    dados_obj = [Dado(10) for _ in range(input.dados)] #Son todos dados de 1D10
    tirada = Tirada_CWoD_20(dados=dados_obj, dificultad=input.dificultad)
    tiradas_guardadas[tirada_id] = tirada
    return {
        "tirada_id": tirada_id,
        "resultado": tirada.resultadoTirada
    }

# Otra petición POST si aplica la regla de 10 en el resultado guardado de la tirada anterior.
@app.post("/tirada/wod20/regla10/{tirada_id}")
def aplicar_regla_del_diez(tirada_id: str):
    tirada = tiradas_guardadas.get(tirada_id)

    if tirada is None:
        return JSONResponse(status_code=404, content={"error": "Tirada no encontrada"})

    nuevos_valores = tirada.tirada_regla_del_diez()
    tirada.evaluar_exitos()  # Recalcula los éxitos incluyendo los nuevos dados

    return {
        "valores_sumados_por_regla10": nuevos_valores,
        "resultado_actualizado": tirada.resultadoTirada
    }