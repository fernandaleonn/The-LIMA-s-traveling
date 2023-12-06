from itertools import permutations

def city_permutation(cities):
   """Funtion that generates all the permutations of all the cities that travel """
    all_permutations = permutations(range(1, cities))
    for permutation in all_permutations:
        yield (0,) + permutation + (0,)

def cost(matrix_distance, route):
   """Gives you theprice of all the routes tha we have generated in city permutations """
    total_dist = 0
    for i in range(len(route) - 1):
        total_dist += matrix_distance[route[i]][route[i + 1]]
    return total_dist


def salesman_traveling_with_pruning(cities, matrix_distance):
   """ Defines a supreme called and generate an empty vector to compare """
    OptC = float('inf')
    OptX = []



    def prune(route, cost_so_far):
        """ Auxiliary function of salesman_traveling_with_pruning that returns the optimal      
        solution implementing the pruning method"""
        nonlocal OptC, OptX
        if cost_so_far >= OptC:
            return True
        return False


    # Función recursiva que busca la ruta óptima
    def recursive_search(route, cost_so_far):
        nonlocal OptC, OptX

        if len(route) == cities:
            route_with_zero = route + (0,)
            C = cost(matrix_distance, route_with_zero)
            if C < OptC:
                OptC = C6
                OptX = route_with_zero
            return

        for city in range(1, cities):
            if city not in route and not prune(route + (city,)+(0,), cost_so_far + matrix_distance[route[-1]][city]):
                recursive_search(route + (city,), cost_so_far + matrix_distance[route[-1]][city])


    # Llamada inicial para iniciar la búsqueda
    recursive_search((0,), 0)
    return OptC, OptX
