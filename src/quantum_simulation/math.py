import math

import numpy as np
from numpy import ndarray

from quantum_simulation import Transformations
from quantum_simulation import States


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
    a = tensor_product(States.ZERO, States.ZERO).reshape((4, 1))
    print(a)
    b = tensor_product(States.ZERO, States.ONE)
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
            (state[0] * States.ZZ + state[1] * States.ZO))


def main():
    """
    main
    """
    print(apply(Transformations.HADAMARD, Transformations.HADAMARD))

    x = np.array([1, 0])
    y = np.array([1, 0])

    print(tensor_product(x, y))
    print(tensor_product(Transformations.HADAMARD, Transformations.HADAMARD))

    bit = np.array([1, 0])
    print(bit)
    print(apply(Transformations.PAULI_I, bit))
    print(apply(Transformations.PAULI_X, bit))
    print(apply(Transformations.PAULI_Y, bit))
    print(apply(Transformations.PAULI_Z, bit))
    print(apply(Transformations.HADAMARD, bit))

    # generate Bell State
    x = apply(Transformations.HADAMARD, States.ZERO)
    print(x)
    xy = tensor_product(x, States.ZERO)
    print(xy)
    print(apply(Transformations.CNOT, xy))

    print("---")
    print(States.BELL)
    print(probability(States.ZERO, States.ZERO))
    print(probability(States.ONE, States.ZERO))
    print(probability(States.ONE, States.ONE))

    print(probability(States.BELL, States.ZZ))
    print(probability(States.BELL, States.ZO))
    print(probability(States.BELL, States.OZ))
    print(probability(States.BELL, States.OO))

    print(".---")
    print(prob(States.BELL))

    print(calc_angle_to_zero(np.array([2, 2])) / (2 * math.pi) * 360)
    print(length(np.array([1, 1, 1])))

    print(calc_angle_to_zero(np.array([1, 0])) / (2 * math.pi) * 360)
    print(bit_prob(np.array([1, 0])))
    print(bit_prob(np.array([1, 1])))
    print(bit_prob(States.PLUS))
    print(bit_prob(States.MINUS))
    print(bit_prob(States.MINUS))

    print(prob_first_digit_zero(tensor_product(States.PLUS, States.PLUS)))
    print(prob_first_digit_zero(States.BELL))

    print(tensor_product(States.PLUS, States.PLUS))
    print(tensor_product(States.MINUS, States.MINUS))


if __name__ == "__main__":
    main()
