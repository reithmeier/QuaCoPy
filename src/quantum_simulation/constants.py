import math
from enum import Enum

import numpy
import numpy as np


class Constants:
    """
    Constants

    contains bit states and transformation matrices
    """

    ZERO = np.array([1, 0]).reshape((2, 1))
    """
    |0> zero state
    """

    ONE = np.array([0, 1]).reshape((2, 1))
    """
    |1> one state
    """

    ZZ = np.array([1, 0, 0, 0]).reshape((4, 1))
    """
    |00> state
    """

    ZO = np.array([0, 1, 0, 0]).reshape((4, 1))
    """
    |01> state
    """

    OZ = np.array([0, 0, 1, 0]).reshape((4, 1))
    """
    |10> state
    """

    OO = np.array([0, 0, 0, 1]).reshape((4, 1))
    """
    |11> State
    """

    PLUS = np.array([1 / math.sqrt(2), 1 / math.sqrt(2)]).reshape((2, 1))
    """
    |+> plus state
    """

    MINUS = np.array([1 / math.sqrt(2), -1 / math.sqrt(2)]).reshape((2, 1))
    """
    |-> minus state
    """

    PAULI_I = np.array([[1, 0],
                        [0, 1]])
    """
    identity
    """

    PAULI_X = np.array([[0, 1],
                        [1, 0]])
    """
    exchange
    """

    #
    PAULI_Y = np.array([[0, 1],
                        [-1, 0]])
    """
    identity with negative
    """

    PAULI_Z = np.array([[1, 0],
                        [0, -1]])
    """
    exchange with negative
    """

    HADAMARD = (1 / math.sqrt(2)) * np.array([[1, 1],
                                              [1, -1]])
    """
    Hadamard Matrix
    """

    HADAMARD_2BIT = 1 / 2 * np.array([[1, 1, 1, 1],
                                      [1, -1, 1, -1],
                                      [1, 1, -1, -1],
                                      [1, -1, -1, 1]])
    """
    2 bit Hadamard Matrix H|00> = H|0> x H|0>
    """

    BELL = np.array([1 / math.sqrt(2), 0, 0, 1 / math.sqrt(2)]).reshape((4, 1))
    """
    Bell state
    """

    CNOT = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]
    ])
    """
    Constant Not
    """


def main():
    """
    main
    """


if __name__ == "__main__":
    main()
