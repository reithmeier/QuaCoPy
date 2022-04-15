"""
QBit
"""

import numpy as np
from numpy import ndarray

from quantum_simulation import math as qmath


class QBit:
    """
    QBit

    Represents a Quantum Bit
    """

    __state = np.zeros(2)
    """
    super position in 0 and 1
    """

    def __init__(self, zero_state: float, one_state: float) -> None:
        """
        :param zero_state: position in dimension 0
        :param one_state: position in dimension 1
        """
        super().__init__()
        self.__state[0] = zero_state
        self.__state[1] = one_state
        if not qmath.is_valid(self.__state):
            raise ValueError(f"State {zero_state}|0> + {one_state}|0> is not valid.")

    def __getstate__(self) -> ndarray:
        return self.__state

    def __str__(self) -> str:
        return f"{self.__state[0]}|0> + {self.__state[1]}|1>"
