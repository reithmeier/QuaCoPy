
import numpy as np
from numpy import ndarray


class QBit:
    """
    QBit

    Represents a Quantum Bit
    """

    __state = np.array([0, 1])  # [a|0>, b|1>]

    def __init__(self, state: ndarray = None) -> None:
        super().__init__()
        if state is not None and state.size > 0:
            self.__state = state

    def __getstate__(self) -> ndarray:
        return self.__state

    def __str__(self) -> str:
        return f"{self.__state[0]}|0> + {self.__state[1]}|1>"


def main():
    """
    main
    """
    bit = QBit(np.array([1, 0]))
    print(bit)
    print(bit.__getstate__())
    bit = QBit(np.array([0.9, 0.1]))
    print(bit)
    bit = QBit()
    print(bit)


if __name__ == "__main__":
    main()
