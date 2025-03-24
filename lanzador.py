import math
from Estrella import Estrella
from Galaxia import Galaxia

def distancia(estrella1, estrella2):
    """
    Calcula la distancia entre dos estrellas en el espacio 3D.

    Parámetros:
    estrella1 (tuple): Coordenadas (x, y, z) de la primera estrella.
    estrella2 (tuple): Coordenadas (x, y, z) de la segunda estrella.

    Retorna:
    float: La distancia entre las dos estrellas.
    """
    x1, y1, z1 = estrella1
    x2, y2, z2 = estrella2
    
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return distancia


def galaxia(estrella):
    """
    Determina la galaxia basada en las coordenadas de la estrella.

    Parámetros:
    estrella (Estrella): La estrella cuya galaxia se quiere determinar.

    Retorna:
    str: El nombre de la galaxia.
    """
    if estrella.x > 0 and estrella.y > 0 and estrella.z > 0:
        return "Galaxia A"
    elif estrella.x < 0 and estrella.y < 0 and estrella.z < 0:
        return "Galaxia B"
    else:
        return "Galaxia C"
    

def estrella_mas_lejos(estrellas):
    """
    Determina la estrella más lejana de una lista de estrellas desde el origen (0, 0, 0).

    Parámetros:
    estrellas (list): Lista de objetos Estrella.

    Retorna:
    Estrella: La estrella más lejana.
    """
    origen = (0, 0, 0)
    distancias = {estrella: distancia((estrella.x, estrella.y, estrella.z), origen) for estrella in estrellas}
    estrella_mas_lejos = max(distancias, key=distancias.get)
    return estrella_mas_lejos

", imprimir_estrellas, determinar_galaxias, calcular_distancias, encontrar_estrella_mas_lejos"


def crear_estrellas():
    """
    Crea una lista de estrellas con coordenadas aleatorias.

    Retorna:
    list: Lista de objetos Estrella.
    """
    estrellas = []
    for i in range(10):
        estrella = Estrella()
        estrellas.append(estrella)
    return estrellas

def imprimir_estrellas(estrellas):
    """
    Imprime las coordenadas de las estrellas en la lista.

    Parámetros:
    estrellas (list): Lista de objetos Estrella.
    """
    for estrella in estrellas:
        print(estrella)

def determinar_galaxias(estrellas):
    """
    Determina la galaxia de cada estrella en la lista.

    Parámetros:
    estrellas (list): Lista de objetos Estrella.
    """
    for estrella in estrellas:
        print(f"{estrella} está en la {galaxia(estrella)}")

def calcular_distancias(estrellas):
    """
    Calcula la distancia entre todas las estrellas en la lista.

    Parámetros:
    estrellas (list): Lista de objetos Estrella.

    Retorna:
    dict: Diccionario con las distancias entre cada par de estrellas.
    """
    distancias = {}
    for i, estrella1 in enumerate(estrellas):
        for estrella2 in estrellas[i+1:]:
            dist = distancia((estrella1.x, estrella1.y, estrella1.z), (estrella2.x, estrella2.y, estrella2.z))
            distancias[(estrella1, estrella2)] = dist
    return distancias

def encontrar_estrella_mas_lejos(estrellas):
    """
    Determina la estrella más lejana de una lista de estrellas desde el origen (0, 0, 0).

    Parámetros:
    estrellas (list): Lista de objetos Estrella.

    Retorna:
    Estrella: La estrella más lejana.
    """
    origen = (0, 0, 0)
    distancias = {estrella: distancia((estrella.x, estrella.y, estrella.z), origen) for estrella in estrellas}
    estrella_mas_lejos = max(distancias, key=distancias.get)
    return estrella_mas_lejos





