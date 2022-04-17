"""
Algorithms
"""
import math

import numpy as np

from quantum_simulation.constants import states, transformations
from quantum_simulation import math as qmath


def deutsch_algorithm(unknown_function: np.ndarray):
    """
    checks if an unknown function Uf is constant or balanced
    constant:
    a -> c
    b -> c
    balanced:
    a -> c
    b -> d

    Deutsch Algorithm in logic gate notation:

    |0> ---- H ---- |''''| ---- H ---- measure
                    | Uf |
    |1> ---- H ---- |____| ----------- ignore

                 |          |       |
                 |          |       |
               |+->       Uf|+->   (H x I)*(Uf|+->)

    :param unknown_function: function represented as 4 x 4 matrix
    :return: "constant" if func is constant, "balanced" if func is balanced
    """

    if unknown_function.shape != (4, 4):
        raise ValueError("Function must have shape (4,4)")

    # get |+->
    plus_minus = states.PM

    # apply function Uf to pm
    # Uf|+->
    applied = qmath.apply(unknown_function, plus_minus)

    # expand Hadamard with I
    # (H x I)
    hadamard_identity = qmath.tensor_product(transformations.H, transformations.I)

    # apply Hadamard previous result
    # (H x I)*(Uf|+->)
    applied = qmath.apply(hadamard_identity, applied)

    # look at first qbit
    zero_zero = applied[0]  # |00>
    zero_one = applied[1]  # |01>
    # ignore |10> |11>

    if math.isclose(zero_zero, 0) and math.isclose(zero_one, 0):
        return "balanced"
    return "constant"
