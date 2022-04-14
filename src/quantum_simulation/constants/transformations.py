"""
Transformation Matrices
"""
import math

import numpy as np

I = PAULI_I = np.array([[1, 0], [0, 1]])
"""
identity
"""

X = PAULI_X = np.array([[0, 1], [1, 0]])
"""
exchange
"""

Y = PAULI_Y = np.array([[0, 1], [-1, 0]])
"""
identity with negative
"""

Z = PAULI_Z = np.array([[1, 0], [0, -1]])
"""
exchange with negative
"""

H = HADAMARD = (1 / math.sqrt(2)) * np.array([[1, 1], [1, -1]])
"""
Hadamard Matrix
"""

HH = HADAMARD_2BIT = (
    1 / 2 * np.array([[1, 1, 1, 1], [1, -1, 1, -1], [1, 1, -1, -1], [1, -1, -1, 1]])
)
"""
2 bit Hadamard Matrix H|00> = H|0> x H|0>
"""

CNOT = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
"""
Constant Not
"""
