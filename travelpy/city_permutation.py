from itertools import permutations

def city_permutation(cities):
    """Function that generates all the permutations of the cities to be traveled"""
    all_permutations = permutations(range(1, cities)) 
    for permutation in all_permutations:
        yield (0,) + permutation + (0,)
