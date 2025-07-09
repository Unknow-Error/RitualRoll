from pdfrw import PdfReader

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

def mapear_campos_PDF_CWoD_a_JSON(datos, diccionario_MAPEO):
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
    salida.update(compactar_dots_CWoD(datos))

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