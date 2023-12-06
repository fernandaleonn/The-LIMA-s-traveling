from itertools import permutations

def city_permutation(cities):
   """Generator that generates all the permutations of the cities to be traveled"""
    all_permutations = permutations(range(1, cities))
    for permutation in all_permutations:
        yield (0,) + permutation + (0,)

def cost(matrix_distance, route):
   """Gives you the prices of all the routes that we have generated in city permutations."""
    total_dist = 0
    for i in range(len(route) - 1):
        total_dist += matrix_distance[route[i]][route[i + 1]]
    return total_dist


def salesman_traveling_with_pruning(cities, matrix_distance):
   """Define a supreme and generates an empty vector for comparison"""
    OptC = float('inf')
    OptX = []



    def prune(route, cost_so_far):
        """ Auxiliary function for the traveling salesman problem with pruning, 
        returning the optimal solution by implementing the pruning method."""
        nonlocal OptC, OptX
        if cost_so_far >= OptC:
            return True
        return False


    def recursive_search(route, cost_so_far):
       """Search for the best route among all possible cases """ 
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

    recursive_search((0,), 0)
    return OptC, OptX
