from Galaxia import Galaxia
from lanzador import distancia, crear_estrellas, imprimir_estrellas, determinar_galaxias, calcular_distancias, encontrar_estrella_mas_lejos

if __name__ == "__main__":
    # Creación de estrellas
    estrellas = crear_estrellas()

    # Imprimir estrellas
    imprimir_estrellas(estrellas)

    # Determinar galaxias
    determinar_galaxias(estrellas)

    # Calcular distancias
    distancias = calcular_distancias(estrellas)
    for (estrella1, estrella2), dist in distancias.items():
        print(f"Distancia entre {estrella1} y {estrella2}: {dist}")

    # (Opcional) Encontrar la estrella más lejos del origen
    estrella_mas_lejos = encontrar_estrella_mas_lejos(estrellas)
    print(f"La estrella más lejos del origen es: {estrella_mas_lejos}")

    # Determinar la galaxia de una estrella específica
    estrella_especifica = estrellas[0]  # Puedes cambiar el índice según sea necesario
    galaxia = determinar_galaxias([estrella_especifica])
    print(f"La galaxia de la estrella {estrella_especifica} es: {galaxia}")

    # Crear una galaxia
    galaxia = Galaxia()
    galaxia.agregar_estrella(estrella_especifica)
    print(f"Galaxia: {galaxia}")
    print(f"Estrellas en la galaxia: {galaxia.estrellas}")
    print(f"La galaxia de la estrella {estrella_especifica} es: {galaxia.estrellas[0]}")

    # (Opcional) Crear una galaxia con estrellas específicas
    estrellas = crear_estrellas()
    galaxia = Galaxia()
    for estrella in estrellas:
        galaxia.agregar_estrella(estrella)
    print(f"Galaxia: {galaxia}")
    print(f"Estrellas en la galaxia: {galaxia.estrellas}")
    for estrella in galaxia.estrellas:
        print(f"La galaxia de la estrella {estrella} es: {galaxia.estrellas[0]}")

    # (Opcional) Crear una galaxia con estrellas específicas y determinar la galaxia de una estrella específica
    estrellas = crear_estrellas()
    galaxia = Galaxia()
    for estrella in estrellas:
        galaxia.agregar_estrella(estrella)
    estrella_especifica = estrellas[0]
    galaxia_estrella = determinar_galaxias([estrella_especifica])
    print(f"Galaxia: {galaxia}")
    print(f"Estrellas en la galaxia: {galaxia.estrellas}")
    print(f"La galaxia de la estrella {estrella_especifica} es: {galaxia_estrella}")

    # (Opcional) Crear una galaxia con estrellas específicas y determinar la galaxia de todas las estrellas
    estrellas = crear_estrellas()
    galaxia = Galaxia()
    for estrella in estrellas:
        galaxia.agregar_estrella(estrella)
    galaxia_estrellas = determinar_galaxias(galaxia.estrellas)
    print(f"Galaxia: {galaxia}")
    print(f"Estrellas en la galaxia: {galaxia.estrellas}")
    for estrella in galaxia.estrellas:
        print(f"La galaxia de la estrella {estrella} es: {galaxia_estrellas[estrella]}")


    # Calcular la distancia entre dos estrellas específicas
    estrella1 = estrellas[0]
    estrella2 = estrellas[1]
    dist = distancia(estrella1, estrella2)
    print(f"Distancia entre {estrella1} y {estrella2}: {dist}")

    
