import numpy as np
from itertools import permutations

def matrix_generator(n):
    # Generar una matriz aleatoria 20x20 de enteros entre 1 y 50
    random_matrix = np.random.randint(1, 50, size=(n, n))

    # Establecer la diagonal en ceros
    np.fill_diagonal(random_matrix, 0)

    # Hacer la matriz simétrica
    symmetric_matrix = (random_matrix + random_matrix.T) // 2
    return symmetric_matrix.tolist()

