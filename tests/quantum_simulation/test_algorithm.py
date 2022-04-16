"""
algorithm tests
"""
import string

import numpy as np
import pytest

from quantum_simulation import algorithm
from quantum_simulation.constants import transformations


@pytest.mark.parametrize(
    "unknown_function, expected",
    [
        (
            np.array(
                [
                    [0, 1, 0, 0],
                    [1, 0, 0, 0],
                    [0, 0, 0, 1],
                    [0, 0, 1, 0],
                ]
            ),
            "constant",
        ),
        (
            np.array(
                [
                    [1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1],
                ]
            ),
            "constant",
        ),
        (
            np.array(
                [
                    [1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 0, 1],
                    [0, 0, 1, 0],
                ]
            ),
            "balanced",
        ),
        (
            np.array(
                [
                    [0, 0, 0, 1],
                    [0, 0, 1, 0],
                    [0, 1, 0, 0],
                    [1, 0, 0, 0],
                ]
            ),
            "constant",
        ),
        (
            np.array(
                [
                    [0, 0, 1, 0],
                    [0, 0, 0, 1],
                    [0, 1, 0, 0],
                    [1, 0, 0, 0],
                ]
            ),
            "balanced",
        ),
        (transformations.CNOT, "balanced"),
    ],
)
def test_deutsch_algorithm(unknown_function: np.ndarray, expected: string):
    """test valid inputs"""
    # given
    # when
    result = algorithm.deutsch_algorithm(unknown_function)
    # then
    assert result == expected


@pytest.mark.parametrize(
    "unknown_function",
    [
        np.array(
            [
                [1],
            ]
        ),
        np.array(
            [
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1],
            ]
        ),
        np.array(
            [
                [1, 0],
                [0, 1],
            ]
        ),
        np.array(
            [
                [0, 0, 0, 0, 1],
                [0, 0, 0, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 1, 0, 0, 0],
                [1, 0, 0, 0, 0],
            ]
        ),
        np.array([]),
    ],
)
def test_deutsch_algorithm_throws(unknown_function: np.ndarray):
    """test invalid inputs"""
    # given
    # when
    # then
    with pytest.raises(ValueError):
        algorithm.deutsch_algorithm(unknown_function)
