"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    datos = {}

    with open("data.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            columnas = linea.strip().split(",")
            letra = columnas[0]
            valor = int(columnas[1])

            if letra not in datos:
                datos[letra] = [valor, valor]  # [máximo, mínimo]
            else:
                if valor > datos[letra][0]:
                    datos[letra][0] = valor
                if valor < datos[letra][1]:
                    datos[letra][1] = valor

    resultado = []

    for letra in sorted(datos):
        resultado.append((letra, datos[letra][0], datos[letra][1]))

    return resultado