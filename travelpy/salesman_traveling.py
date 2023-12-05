from itertools import permutations

def city_permutation(cities):
    all_permutations = permutations(range(1, cities))  # Genera todas las permutaciones posibles excepto (0, ...)
    for permutation in all_permutations:
        yield (0,) + permutation + (0,)  # Agrega 0 al inicio y al final de la permutación

def cost(cities, matrix_distance, route):
    total_dist = 0
    for i in range(len(route) - 1):
        total_dist += matrix_distance[route[i]][route[i + 1]]
    return total_dist

def salesman_traveling(cities, matrix_distance):
    OptC = float('inf')  # Inicializar con un valor alto para comparación
    OptX = []

    for route in city_permutation(cities):
        C = cost(cities, matrix_distance, route)
        if C < OptC:
            OptC = C
            OptX = route

    return OptC, OptX
