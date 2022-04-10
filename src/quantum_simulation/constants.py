import math
from enum import Enum

import numpy
import numpy as np


class Constants:
    """
    Constants

    contains bit states and transformation matrices
    """

    # |0> zero state
    ZERO = np.array([1, 0])

    # |1> one state
    ONE = np.array([0, 1])

    # |+> plus state
    PLUS = np.array([1 / math.sqrt(2), 1 / math.sqrt(2)])

    # |-> minus state
    MINUS = np.array([1 / math.sqrt(2), -1 / math.sqrt(2)])

    # identity
    PAULI_I = np.array([[1, 0],
                        [0, 1]])

    # exchange
    PAULI_X = np.array([[0, 1],
                        [1, 0]])

    # identity with negative
    PAULI_Y = np.array([[0, 1],
                        [-1, 0]])

    # exchange with negative
    PAULI_Z = np.array([[1, 0],
                        [0, -1]])

    # Hadamard Matrix
    HADAMARD = (1 / math.sqrt(2)) * np.array([[1, 1],
                                              [1, -1]])

    # Bell state
    BELL = np.array([1 / math.sqrt(2), 0, 0, 1 / math.sqrt(2)])

    # Constant Not
    CNOT = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]
    ])


def main():
    """
    main
    """


if __name__ == "__main__":
    main()
