from hojaPersonajes import (
    extraer_todos_los_campos_pdf,
    compactar_dots_CWoD,
    mapear_campos_PDF_CWoD_a_JSON,
    expandir_dots_CWoD,
    reconstruir_campos_CWoD_pdf,
    completar_hoja_personaje_pdf
)

from mage_CWoD_20 import(
    CAMPO_MAP_MAGO_OFICIAL,
    DOT_GRUPOS_MAGO_OFICIAL,
    DOT_YE_VALUES,
    contar_quintaesencia_y_paradoja
)

# Paso 1: Parsear campos del PDF
ruta_input_prueba = "/home/Nephelim/Documentos/Programacion/VSCodium-Projects/RitualRoll/Reliquias/HojasPersonajes/Mage_The_Ascension_20/M20_4-Page_Official_Interactive-prueba2.pdf"
campos_extraidos = extraer_todos_los_campos_pdf(ruta_input_prueba)

# Paso 2: Compactar a JSON
json_jugador = mapear_campos_PDF_CWoD_a_JSON(campos_extraidos, CAMPO_MAP_MAGO_OFICIAL, DOT_GRUPOS_MAGO_OFICIAL)
json_jugador.update(contar_quintaesencia_y_paradoja(campos_extraidos))

# (Opcional: imprimir lo que se compactó)
print("JSON compactado:")
for k, v in json_jugador.items():
    print(f"{k}: {v}")

# Paso 3: Convertir JSON a formato editable del PDF
campos_para_pdf = reconstruir_campos_CWoD_pdf(json_jugador, CAMPO_MAP_MAGO_OFICIAL, DOT_GRUPOS_MAGO_OFICIAL)

# Paso 4: Completar nuevo PDF
ruta_input_blanco = "/home/Nephelim/Documentos/Programacion/VSCodium-Projects/RitualRoll/Reliquias/HojasPersonajes/Mage_The_Ascension_20/M20_4-Page_Official_Interactive.pdf"
ruta_output = "/home/Nephelim/Documentos/Programacion/VSCodium-Projects/RitualRoll/Reliquias/Generados/output_completado.pdf"
completar_hoja_personaje_pdf(
    ruta_input_blanco,
    ruta_output,
    campos_para_pdf
)

print("✅ PDF generado como 'output_completado.pdf'")