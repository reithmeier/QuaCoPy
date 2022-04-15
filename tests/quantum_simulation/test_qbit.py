import math

import pytest
import numpy as np
from quantum_simulation import QBit


@pytest.mark.parametrize(
    "zero_state,one_state,expected",
    [
        (1, 0, np.array([1, 0])),
        (0, 1, np.array([0, 1])),
        (-1, 0, np.array([-1, 0])),
        (0, -1, np.array([0, -1])),
        (
            1 / math.sqrt(2),
            1 / math.sqrt(2),
            np.array([1 / math.sqrt(2), 1 / math.sqrt(2)]),
        ),
        (
            -1 / math.sqrt(2),
            1 / math.sqrt(2),
            np.array([-1 / math.sqrt(2), 1 / math.sqrt(2)]),
        ),
        (
            1 / math.sqrt(2),
            -1 / math.sqrt(2),
            np.array([1 / math.sqrt(2), -1 / math.sqrt(2)]),
        ),
        (
            -1 / math.sqrt(2),
            -1 / math.sqrt(2),
            np.array([-1 / math.sqrt(2), -1 / math.sqrt(2)]),
        ),
    ],
)
def test_init_no_throw(zero_state, one_state, expected):
    # given
    # when
    result = QBit(zero_state, one_state)
    # then
    assert np.array_equal(result.__getstate__(), expected)


@pytest.mark.parametrize(
    "zero_state,one_state",
    [(1, 1), (0, 0), (-1, -1), (0.5, 0.5)],
)
def test_init_throw(zero_state, one_state):
    # given
    # when
    # then
    with pytest.raises(ValueError):
        QBit(zero_state, one_state)
