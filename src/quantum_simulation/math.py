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


def probability_zero(state):
    a = tensor_product(Constants.ZERO, Constants.ZERO).reshape((4, 1))
    print(a)
    b = tensor_product(Constants.ZERO, Constants.ONE)
    print(b)
    return apply(state, a)


def probability(state1: ndarray, state2: ndarray):
    return apply(state1.reshape(state1.size), state2.reshape((state2.size, 1)))


def length(state):
    """
    calculates the length of a quantum state using the pythagorean theorem in an euclidean space
    d1^2+d2^2+d3^3+... = l^2
    :param state: n digit quantum state
    :return: length of state
    """
    squares = np.power(state, 2)
    return math.sqrt(np.sum(squares))


def calc_angle_to_zero(qbit):
    """
    calculates the angle between the qbit vector and the zero state |0> = (1,0)
    :param qbit: qbit of size 2
    :return: angle between the qbit vector and the zero state
    """
    hypothenuse = length(qbit)
    return math.acos(qbit[0] / hypothenuse)


def bit_prob(qbit: ndarray):
    """
    calculates probability that a qbit has the Zero state |0> = (1,0)
    :param qbit: qbit of size 2
    :return: probability that the qbit is of state 0
    """
    if qbit.size > 2:
        return prob(qbit)

    angle = calc_angle_to_zero(qbit)

    cos_angle = math.cos(angle)
    return cos_angle * cos_angle


def prob_first_digit_zero(state: ndarray):
    """
    calculates the probability that the first digit of the state ist zero state
    P(d0 == |0>) = d00^2 + d01^2
    :param state: quantum state
    :return:probability that the first digit of the state ist zero state
    """
    return state[0] * state[0] + state[1] * state[1]


def prob(state: ndarray):
    state = state.reshape(state.size)
    print(state)

    return (1 / math.sqrt(state[0] * state[0] + state[1] * state[1]) *
            (state[0] * Constants.ZZ + state[1] * Constants.ZO))


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

    # generate Bell State
    x = apply(Constants.HADAMARD, Constants.ZERO)
    print(x)
    xy = tensor_product(x, Constants.ZERO)
    print(xy)
    print(apply(Constants.CNOT, xy))

    print("---")
    print(Constants.BELL)
    print(probability(Constants.ZERO, Constants.ZERO))
    print(probability(Constants.ONE, Constants.ZERO))
    print(probability(Constants.ONE, Constants.ONE))

    print(probability(Constants.BELL, Constants.ZZ))
    print(probability(Constants.BELL, Constants.ZO))
    print(probability(Constants.BELL, Constants.OZ))
    print(probability(Constants.BELL, Constants.OO))

    print(".---")
    print(prob(Constants.BELL))

    print(calc_angle_to_zero(np.array([2, 2])) / (2 * math.pi) * 360)
    print(length(np.array([1, 1, 1])))

    print(calc_angle_to_zero(np.array([1, 0])) / (2 * math.pi) * 360)
    print(bit_prob(np.array([1, 0])))
    print(bit_prob(np.array([1, 1])))
    print(bit_prob(Constants.PLUS))
    print(bit_prob(Constants.MINUS))
    print(bit_prob(Constants.MINUS))

    print(prob_first_digit_zero(tensor_product(Constants.PLUS, Constants.PLUS)))
    print(prob_first_digit_zero(Constants.BELL))


if __name__ == "__main__":
    main()
