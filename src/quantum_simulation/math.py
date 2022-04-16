"""
contains mathematical functions
"""
import random

import math

import numpy as np
from numpy import ndarray

from quantum_simulation.constants import states


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
    return qbit.size == 2 and math.isclose(length(qbit), 1.0)


def length(state: ndarray):
    """
    calculates the length / magnitude of a quantum state
    using the pythagorean theorem in euclidean space
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


def prob_qbit_zero(qbit: ndarray):
    """
    calculates probability that a qbit has the Zero state |0> = (1,0)
    :param qbit: qbit of size 2
    :return: probability that the qbit is of state 0
    """

    return (qbit[0] * qbit[0])[0]


def prob_first_digit_zero(state: ndarray):
    """
    calculates the probability that the first digit of the state ist zero state
    P(d0 == |0>) = d00^2 + d01^2
    :param state: quantum state
    :return:probability that the first digit of the state ist zero state
    """
    return (state[0] * state[0] + state[1] * state[1])[0]


def measure_qbit(qbit: ndarray):
    """
    measure a qbit
    :param qbit: qbit
    :return: 0
    """
    prob = prob_qbit_zero(qbit)
    return random.choices([states.ZERO, states.ONE], [prob, 1 - prob])


def measure_first_digit(state: ndarray):
    """
    measure a 2qbit state
    :param state: 2qbit state
    :return: |0> or |1>
    """
    prob = prob_first_digit_zero(state)
    return np.array(random.choices([states.ZERO, states.ONE], [prob, 1 - prob]))[0]


def main():
    """main"""
    print(measure_qbit(states.ZERO))
    print(measure_qbit(states.ONE))
    print(measure_qbit(states.PLUS))
    print(measure_qbit(states.MINUS))

    print(measure_first_digit(states.ZZ))
    print(measure_first_digit(states.OO))
    print(measure_first_digit(states.PP))
    print(measure_first_digit(states.PM))
    print(measure_first_digit(states.MP))
    print(measure_first_digit(states.MM))


if __name__ == "__main__":
    main()
