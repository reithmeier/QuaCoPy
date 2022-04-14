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


def length(state: ndarray):
    """
    calculates the length of a quantum state using the pythagorean theorem in an euclidean space
    d1^2+d2^2+d3^3+... = l^2
    :param state: n digit quantum state
    :return: length of state
    """
    squares = np.power(state, 2)
    return math.sqrt(np.sum(squares))


def calc_angle_to_zero(qbit: ndarray):
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
    print(apply(transformations.HADAMARD, transformations.HADAMARD))

    x = np.array([1, 0])
    y = np.array([1, 0])

    print(tensor_product(x, y))
    print(tensor_product(transformations.HADAMARD, transformations.HADAMARD))

    bit = np.array([1, 0])
    print(bit)
    print(apply(transformations.PAULI_I, bit))
    print(apply(transformations.PAULI_X, bit))
    print(apply(transformations.PAULI_Y, bit))
    print(apply(transformations.PAULI_Z, bit))
    print(apply(transformations.HADAMARD, bit))

    print(calc_angle_to_zero(np.array([2, 2])) / (2 * math.pi) * 360)
    print(length(np.array([1, 1, 1])))

    print(calc_angle_to_zero(np.array([1, 0])) / (2 * math.pi) * 360)
    print(bit_prob(np.array([1, 0])))
    print(bit_prob(np.array([1, 1])))
    print(bit_prob(states.PLUS))
    print(bit_prob(states.MINUS))
    print(bit_prob(states.MINUS))

    print(prob_first_digit_zero(tensor_product(states.PLUS, states.PLUS)))
    print(prob_first_digit_zero(states.BELL))

    print(tensor_product(states.PLUS, states.PLUS))
    print(tensor_product(states.MINUS, states.MINUS))

    print(tensor_product([1, 1], [1, -1]))
    print(tensor_product([1, -1], [1, 1]))


if __name__ == "__main__":
    main()
