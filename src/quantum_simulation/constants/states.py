import math

import numpy as np


class States:
    """
    States

    contains bit states
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

    PP = 1 / 2 * np.array([1, 1, 1, 1]).reshape((4, 1))
    """
    |++> state
    """

    MM = 1 / 2 * np.array([1, -1, -1, 1]).reshape((4, 1))
    """
    |--> state
    """

    BELL = np.array([1 / math.sqrt(2), 0, 0, 1 / math.sqrt(2)]).reshape((4, 1))
    """
    Bell state
    """
