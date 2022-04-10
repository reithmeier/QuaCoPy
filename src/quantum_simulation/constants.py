import math
from enum import Enum

import numpy
import numpy as np


class Constants:
    ZERO = np.array([1, 0])

    ONE = np.array([0, 1])

    PAULI_I = np.array([[1, 0],
                        [0, 1]])

    PAULI_X = np.array([[0, 1],
                        [1, 0]])

    PAULI_Y = np.array([[0, 1],
                        [-1, 0]])

    PAULI_Z = np.array([[1, 0],
                        [0, -1]])

    HADAMARD = (1 / math.sqrt(2)) * np.array([[1, 1],
                                              [1, -1]])

    BELL = np.array([1 / math.sqrt(2), 0, 0, 1 / math.sqrt(2)])

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
