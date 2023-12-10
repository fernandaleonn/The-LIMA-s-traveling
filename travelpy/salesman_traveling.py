from itertools import permutations

def city_permutation(cities):
    """Function that generates all the permutations of the cities to be traveled"""
    all_permutations = permutations(range(1, cities)) 
    for permutation in all_permutations:
        yield (0,) + permutation + (0,) 

def cost(matrix_distance, route):
    """Gives you the prices of all the routes that we have generated in city permutations."""
    total_dist = 0
    for i in range(len(route) - 1):
        total_dist += matrix_distance[route[i]][route[i + 1]]
    return total_dist

def salesman_traveling(cities, matrix_distance):
    opt_c = float('inf')  # Inicializar con un valor alto para comparación
    opt_x = []

    for route in city_permutation(cities):
        c = cost(matrix_distance, route)
        if c < opt_c:
            opt_c = c
            opt_x = route

    return opt_c, opt_x
