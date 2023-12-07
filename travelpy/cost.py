
def cost(matrix_distance, route):
    """Gives you the prices of all the routes that we have generated in city permutations"""
    total_dist = 0
    for i in range(len(route) - 1):
        total_dist += matrix_distance[route[i]][route[i + 1]]
    return total_dist
