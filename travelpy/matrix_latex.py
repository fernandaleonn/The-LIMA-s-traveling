"""
Module for printing a matrix in LaTeX format using SymPy.
"""

from sympy import Matrix, init_printing

def print_latex_matrix(matriz):
    """ Print a matrix in latex format"""
    init_printing(use_latex=True)
    matriz_sympy = Matrix(matriz)
    display(matriz_sympy)
