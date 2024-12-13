def promedio(lista):
    if not lista:
        raise ValueError("La lista está vacía.")
    suma_elementos = sum(lista)
    return suma_elementos / len(lista)


def mediana(lista):
    if not lista:
        raise ValueError("La lista está vacía.")
    datos_ordenados = sorted(lista)
    cantidad_datos = len(datos_ordenados)

    if cantidad_datos % 2 == 0:
        elementos_centrales = [datos_ordenados[(cantidad_datos // 2) - 1], datos_ordenados[cantidad_datos // 2]]
        return promedio(elementos_centrales)
    else:
        return datos_ordenados[cantidad_datos // 2]


def moda(lista):
    if not lista:
        raise ValueError("La lista está vacía.")
    frecuencias = {}
    for elemento in lista:
        frecuencias[elemento] = frecuencias.get(elemento, 0) + 1

    maxima_frecuencia = max(frecuencias.values())
    return [key for key, value in frecuencias.items() if value == maxima_frecuencia]


def rango(lista):
    if not lista:
        raise ValueError("La lista está vacía.")
    datos_ordenados = sorted(lista)
    return datos_ordenados[-1] - datos_ordenados[0]


def varianza(lista):
    if not lista:
        raise ValueError("La lista está vacía.")
    promedio_lista = promedio(lista)
    return sum((elem - promedio_lista) ** 2 for elem in lista) / len(lista)


def desviacion_estandar(lista):
    return varianza(lista) ** 0.5


def rango_intercuartilico(lista):
    if not lista:
        raise ValueError("La lista está vacía.")
    lista_ordenada = sorted(lista)
    cantidad_datos = len(lista_ordenada)
    if cantidad_datos % 2 == 0:
        Q1 = promedio([lista_ordenada[(cantidad_datos // 4) - 1], lista_ordenada[cantidad_datos // 4]])
        Q3 = promedio([lista_ordenada[(3 * cantidad_datos // 4) - 1], lista_ordenada[3 * cantidad_datos // 4]])
    else:
        Q1 = lista_ordenada[cantidad_datos // 4]
        Q3 = lista_ordenada[(3 * cantidad_datos) // 4]
    return Q3 - Q1


def MAD(lista):
    if not lista:
        raise ValueError("La lista está vacía.")
    med = mediana(lista)
    desviaciones = [abs(elem - med) for elem in lista]
    return mediana(desviaciones)


def covarianza(x, y):
    if len(x) != len(y):
        raise ValueError("Las listas deben tener la misma longitud.")
    promedio_x = promedio(x)
    promedio_y = promedio(y)
    suma_productos = sum((i - promedio_x) * (j - promedio_y) for i, j in zip(x, y))
    return suma_productos / len(x)


def coeficiente_correlacion(x, y):
    return covarianza(x, y) / (desviacion_estandar(x) * desviacion_estandar(y))
