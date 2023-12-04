def salesman_traveling(cities, matrix_distance):
    OptC = float('inf')  # Inicializar con un valor alto para comparación
    OptX = []

    for route in city_permutation(cities):
        C = cost(cities, matrix_distance, route)
        if C < OptC:
            OptC = C
            OptX = route

    return OptC, OptX
