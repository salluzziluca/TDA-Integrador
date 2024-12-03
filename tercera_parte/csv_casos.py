def procesar_archivo(nombre_test):
    with open(nombre_test) as archivo:
        lineas = [linea.strip() for linea in archivo if not linea.startswith("#")]
    
    # Separar las secciones basándonos en líneas completamente vacías
    contenido = "\n".join(lineas).strip()
    secciones = [seccion.splitlines() for seccion in contenido.split("\n\n") if seccion.strip()]
    
    # Verificar que haya suficientes secciones
    if len(secciones) < 3:
        raise ValueError("El archivo no tiene el formato esperado con tres secciones separadas por líneas en blanco.")
    
    # Convertir las secciones en listas de enteros
    filas = list(map(int, secciones[0]))
    columnas = list(map(int, secciones[1]))
    barcos = list(map(int, secciones[2]))
   
    
    return barcos, filas, columnas
    
    


