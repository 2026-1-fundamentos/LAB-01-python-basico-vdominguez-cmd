"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    suma = {}

    with open("data.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            columnas = linea.strip().split(",")

            valor = int(columnas[1])
            letras = columnas[3].split("|")

            for letra in letras:
                if letra in suma:
                    suma[letra] += valor
                else:
                    suma[letra] = valor

    resultado = {}

    for letra in sorted(suma):
        resultado[letra] = suma[letra]

    return resultado