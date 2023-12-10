"""
Module for solving the Traveling Salesman Problem (TSP) with a pruning method.
"""
from itertools import permutations

def city_permutation(cities):
    """Generator that generates all the permutations of the cities to be traveled"""
    all_permutations = permutations(range(1, cities))
    for permutation in all_permutations:
        yield (0,) + permutation + (0,)

def cost(matrix_distance, route):
    """Gives you the prices of all the routes that we have generated in city permutations"""
    total_dist = 0
    for i in range(len(route) - 1):
        total_dist += matrix_distance[route[i]][route[i + 1]]
    return total_dist

def pruning_method(num_cities, matrix_distance):
    """Defines a supreme and generates an empty vector for comparison"""
    opt_c = float('inf')
    opt_x = []

    def prune(current_cost):
        """Auxiliary function for the traveling salesman problem with pruning,
        returning the optimal solution by implementing the pruning method"""
        nonlocal opt_c, opt_x
        if current_cost >= opt_c:
            return True
        return False
    def recursive_search(route, current_cost):
        """Search for the best route among all possible cases"""
        nonlocal opt_c, opt_x
        if len(route) == num_cities:
            route_with_zero = route + (0,)
            total_cost = cost(matrix_distance, route_with_zero)
            if total_cost < opt_c:
                opt_c = total_cost
                opt_x = route_with_zero
            return
        for city in range(1, num_cities):
            if city not in route and not prune(current_cost +
                                         matrix_distance[route[-1]][city]):
                recursive_search(route + (city,),current_cost + matrix_distance[route[-1]][city])
    recursive_search((0,), 0)
    return opt_c, opt_x
