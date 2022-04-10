import math

import numpy as np
from numpy import ndarray

from quantum_simulation import QBit
from quantum_simulation.constants import Constants


def apply(x, y):
    return np.matmul(x, y)


def tensor_product(x: ndarray, y: ndarray):
    """
    combine 2 matrices by applying
    :param x:
    :param y:
    :return:
    """
    return np.kron(x, y)


def measure_zero(state):
    print(state[0] * state[0])
    print(state[0] + state[1])
    print(1 / math.sqrt(2))
    print(1. / math.sqrt(state[0] * state[0] + state[1] * state[1]))

    return (1. / math.sqrt(state[0] * state[0] + state[1] * state[1])) * (state[0] + state[1])


def measure_one(state):
    return 1. - measure_zero(state)


def measure(state):
    probability_of_zero = measure_zero(state)
    return np.array([probability_of_zero, 1 - probability_of_zero])


def main():
    """
    main
    """
    print(apply(Constants.HADAMARD, Constants.HADAMARD))

    x = np.array([1, 0])
    y = np.array([1, 0])

    print(tensor_product(x, y))
    print(tensor_product(Constants.HADAMARD, Constants.HADAMARD))

    bit = np.array([1, 0])
    print(bit)
    print(apply(Constants.PAULI_I, bit))
    print(apply(Constants.PAULI_X, bit))
    print(apply(Constants.PAULI_Y, bit))
    print(apply(Constants.PAULI_Z, bit))
    print(apply(Constants.HADAMARD, bit))

    print("---")
    print(measure(Constants.BELL))

    print(apply(Constants.CNOT, np.array([
        [1/math.sqrt(2)],
        [0],
        [0],
        [1/math.sqrt(2)]
    ])))

if __name__ == "__main__":
    main()
