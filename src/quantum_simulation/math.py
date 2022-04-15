"""
contains mathematical functions
"""
import math

import numpy as np
from numpy import ndarray

from quantum_simulation.constants import states, transformations


def apply(x, y):
    """
    * apply a matrix to another matrix by matrix multiplication
    * apply a transformation to a state by matrix multiplication
    * apply a transformation to a transformation by matrix multiplication
    * apply a state to a state by matrix multiplication
    Important: matrices and states must have the right dimensions for matrix multiplication
    :param x: first matrix
    :param y: second matrix
    :return: x * y
    """
    return np.matmul(x, y)


def tensor_product(x: ndarray, y: ndarray):
    """
    combine 2 matrices by applying Kronecker product
    e.g.:
    a = [1, 1], b = [1, -1]
    tensor_product(a, b) = [1 * b, 1 * b] = [1, -1, 1, -1]
    :param x: x
    :param y: y
    :return: tensor product of x and y
    """
    return np.kron(x, y)


def is_valid(qbit: ndarray):
    """
    checks if the qbit has a valid state
    :param qbit: qbit
    :return: true, if the state of the qbit is valid
    """
    return qbit.size == 2 and math.isclose(length(qbit), 1.)


def length(state: ndarray):
    """
    calculates the length / magnitude of a quantum state using the pythagorean theorem in euclidean space
    d1^2+d2^2+d3^3+... = l^2
    :param state: n digit quantum state
    :return: length of state
    """
    squares = np.power(state, 2)
    return math.sqrt(np.sum(squares))


def calc_angle_to_zero(qbit: ndarray):
    """
    calculates the angle between the qbit vector and the zero state |0> = (1,0)
    :param qbit: valid qbit of size 2
    :return: angle between the qbit vector and the zero state
    :raises ValueError if the qbit is not valid
    """
    if not is_valid(qbit):
        raise ValueError(f"The QBit {qbit} is not valid.")
    # angle = acos(qbit[0] / hypothenuse)
    # since the hypothenuse is the length of the qbit
    # and the length of a valid qbit is always 1
    # this expression can be minimized to
    return math.acos(qbit[0])


def bit_prob(qbit: ndarray):
    """
    calculates probability that a qbit has the Zero state |0> = (1,0)
    :param qbit: qbit of size 2
    :return: probability that the qbit is of state 0
    """
    if qbit.size > 2:
        return prob_first_digit_zero(qbit)

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

    return (
            1
            / math.sqrt(state[0] * state[0] + state[1] * state[1])
            * (state[0] * states.ZZ + state[1] * states.ZO)
    )


def probability_zero(state: ndarray):
    a = tensor_product(states.ZERO, states.ZERO).reshape((4, 1))
    print(a)
    b = tensor_product(states.ZERO, states.ONE)
    print(b)
    return apply(state, a)


def probability(state1: ndarray, state2: ndarray):
    return apply(state1.reshape(state1.size), state2.reshape((state2.size, 1)))


def main():
    """
    main
    """

    print(is_valid(states.PLUS))
    print(length(states.PLUS))
    print(states.PLUS.size)


if __name__ == "__main__":
    main()
