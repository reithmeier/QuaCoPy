import math

import numpy as np


class Transformations:
    """
    Transformations

    contains transformation matrices
    """

    PAULI_I = np.array([[1, 0], [0, 1]])
    """
    identity
    """

    PAULI_X = np.array([[0, 1], [1, 0]])
    """
    exchange
    """

    PAULI_Y = np.array([[0, 1], [-1, 0]])
    """
    identity with negative
    """

    PAULI_Z = np.array([[1, 0], [0, -1]])
    """
    exchange with negative
    """

    HADAMARD = (1 / math.sqrt(2)) * np.array([[1, 1], [1, -1]])
    """
    Hadamard Matrix
    """

    H = HADAMARD
    """
    Hadamard Matrix
    """

    HADAMARD_2BIT = (
        1 / 2 * np.array([[1, 1, 1, 1], [1, -1, 1, -1], [1, 1, -1, -1], [1, -1, -1, 1]])
    )
    """
    2 bit Hadamard Matrix H|00> = H|0> x H|0>
    """

    HH = HADAMARD_2BIT
    """
    2 bit Hadamard Matrix H|00> = H|0> x H|0>
    """

    CNOT = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
    """
    Constant Not
    """
