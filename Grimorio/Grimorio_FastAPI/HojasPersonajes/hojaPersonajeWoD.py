from pdfrw import PdfReader

def extraer_todos_los_campos_WoD_pdf(ruta_pdf):
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