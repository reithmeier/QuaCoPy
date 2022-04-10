import math

import numpy
import numpy as np


class Transformations:

    @staticmethod
    def pauli_i(x):
        return numpy.matmul(x, np.array([[1, 0],
                                         [0, 1]]))

    @staticmethod
    def pauli_x(x):
        return numpy.matmul(x, np.array([[0, 1],
                                         [1, 0]]))

    @staticmethod
    def pauli_y(x):
        return numpy.matmul(x, np.array([[0, 1],
                                         [-1, 0]]))

    @staticmethod
    def pauli_z(x):
        return numpy.matmul(x, np.array([[1, 0],
                                         [0, -1]]))

    @staticmethod
    def hadamard(x):
        return numpy.matmul(x, np.array([[1 / math.sqrt(2), 1 / math.sqrt(2)],
                                         [1 / math.sqrt(2), -1 / math.sqrt(2)]]))


def main():
    """
    main
    """
    bit = np.array([1, 0])
    print(bit)
    print(Transformations.pauli_i(bit))
    print(Transformations.pauli_x(bit))
    print(Transformations.pauli_y(bit))
    print(Transformations.pauli_z(bit))
    print(Transformations.hadamard(bit))


if __name__ == "__main__":
    main()
