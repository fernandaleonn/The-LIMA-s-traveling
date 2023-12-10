"""
Module to generate a matrix representing the distance between cities.
"""

import numpy as np

def matrix_generator(n):
    """Generate a matrix representing the distance between cities"""
    random_matrix = np.random.randint(1, 50, size=(n, n))
    np.fill_diagonal(random_matrix, 0)
    symmetric_matrix = (random_matrix + random_matrix.T) // 2
    return symmetric_matrix.tolist()
