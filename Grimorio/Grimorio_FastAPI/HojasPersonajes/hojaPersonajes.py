from pdfrw import PdfReader, PdfWriter, PdfDict, PdfName, PdfObject
from mage_CWoD_20 import contar_quintaesencia_y_paradoja, expandir_quintaesenciae_y_paradoja, DOT_YE_VALUES

def extraer_todos_los_campos_pdf(ruta_pdf):
    """
        Función para extraer todos los campos de una hoja de personaje en formato .pdf.
        Retorna un diccionario con cada campo, su valor seleccionado actual y las opciones desplegables si las posee.
    """
    pdf = PdfReader(ruta_pdf)
    campos = {}

    if not pdf.Root.AcroForm or not pdf.Root.AcroForm.Fields:
        return {}

    for campo in pdf.Root.AcroForm.Fields:
        nombre = campo.T[1:-1] if campo.T else None
        valor = campo.V[1:-1] if campo.V else ""
        opciones = campo.Opt if hasattr(campo, "Opt") else None

        if not nombre:
            continue

        if opciones:
            # Limpiar opciones
            opciones_limpias = []
            for opcion in opciones:
                if hasattr(opcion, 'decode'):
                    opciones_limpias.append(opcion.decode())
                elif isinstance(opcion, str):
                    opciones_limpias.append(opcion)
                elif isinstance(opcion, list) and len(opcion) >= 1:
                    opciones_limpias.append(str(opcion[1] if len(opcion) > 1 else opcion[0]))
                else:
                    opciones_limpias.append(str(opcion))

            campos[nombre] = {
                "tipo": "desplegable",
                "valor_actual": valor,
                "opciones": opciones_limpias
            }

        else:
            campos[nombre] = {
                "tipo": "texto",
                "valor_actual": valor
            }

    return campos

def compactar_dots_CWoD(datos, diccionario_DOTS):
    """
        Devuelve un diccionario con los nombres lógicos de cada grupo de dots y su cantidad activa.
        Los "DOTS" son los campos de circulo o cuadrado rellenables en un pdf. Esto permite transformarlos en un valor numérico.
    """
    resultado = {}
    for nombre_logico, lista_dots in diccionario_DOTS.items():
        cantidad = sum(1 for dot in lista_dots if datos.get(dot, {}).get("valor_actual", "") in DOT_YE_VALUES)
        resultado[nombre_logico] = cantidad
    return resultado

def mapear_campos_PDF_CWoD_a_JSON(datos, diccionario_MAPEO, diccionario_DOTS):
    """
        Convierte campos individuales y compacta los dots. Retorna JSON legible.
    """
    salida = {}
    
    # Mapeo directo de campos (texto, desplegables)
    for campo_pdf, nombre_logico in diccionario_MAPEO.items():
        if campo_pdf in datos:
            campo_info = datos[campo_pdf]
            valor = campo_info.get("valor_actual", "")
            if campo_info.get("tipo") == "desplegable":
                salida[nombre_logico] = valor.strip()
            else:
                salida[nombre_logico] = valor.strip()
    
    # Compactar los dots
    salida.update(compactar_dots_CWoD(datos, diccionario_DOTS))

    return salida

def mapear_campos_completo_PDF_CWoD_a_JSON(datos, mapeo):
    """
        Devuelve todas las opciones posibles para construir una UI interactiva, con dots inicializados.
    """
    salida = {}

    # Desplegables vacíos o con opciones
    for campo_pdf, nombre_logico in mapeo.items():
        campo_info = datos.get(campo_pdf)
        if campo_info:
            if campo_info["tipo"] == "desplegable":
                salida[nombre_logico] = {
                    "opciones": campo_info.get("opciones", []),
                    "seleccion": campo_info.get("valor_actual", "").strip()
                }
            else:
                salida[nombre_logico] = campo_info.get("valor_actual", "").strip()
        else:
            salida[nombre_logico] = ""  # por si no existe aún

    # Compactar los dots
    salida.update(compactar_dots_CWoD(datos))

    return salida

def expandir_dots_CWoD(datos_compactados, diccionario_DOTS):
    """
        Devuelve un diccionario con el formato de entrada del PDF a partir de los nombres lógicos de dots.
    """
    resultado = {}
    for nombre_logico, lista_dots in diccionario_DOTS.items():
        cantidad = datos_compactados.get(nombre_logico, 0)
        for i, dot in enumerate(lista_dots):
            resultado[dot] = {
                "tipo": "texto",
                "valor_actual": "Ye" if i < cantidad else ""
            }
    return resultado

def reconstruir_campos_CWoD_pdf(json_jugador, mapeo, diccionario_DOTS):
    campos_pdf = {}

    # Expandir los dots primero (atributos, skills, spheres, etc.)
    campos_pdf.update(expandir_dots_CWoD(json_jugador, diccionario_DOTS))

    # Expandir los qpcheck (quintessence y paradox)
    qdots = json_jugador.get("quintessence_dots", 0)
    pdots = json_jugador.get("paradox_dots", 0)
    campos_pdf.update(expandir_quintaesenciae_y_paradoja(qdots, pdots))

    # Campos mapeados normales
    for pdf_key, json_key in mapeo.items():
        if json_key in json_jugador:
            valor = json_jugador[json_key]
            campos_pdf[pdf_key] = {
                "tipo": "texto",  # en general
                "valor_actual": valor
            }

    return campos_pdf

def completar_hoja_personaje_pdf(ruta_pdf_input, ruta_pdf_output, campos):
    pdf = PdfReader(ruta_pdf_input)
    for campo in pdf.Root.AcroForm.Fields:
        nombre = campo.T[1:-1] if campo.T else None
        if not nombre or nombre not in campos:
            continue

        valor = campos[nombre]["valor_actual"]
        campo.V = PdfObject(f'({valor})')
        campo.AP = None  # Borrar apariencia previa si hay

    PdfWriter().write(ruta_pdf_output, pdf)