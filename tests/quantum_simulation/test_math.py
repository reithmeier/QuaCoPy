import math

import numpy as np
import pytest

from quantum_simulation import math as qmath
from quantum_simulation.constants import states
from quantum_simulation.constants import transformations


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (transformations.HADAMARD, states.ZERO, states.PLUS),
        (transformations.HADAMARD, states.ONE, states.MINUS),
        (transformations.HH, states.ZZ, states.PP),
        (transformations.HH, states.OO, states.MM),
        (transformations.PAULI_I, states.ZERO, states.ZERO),
        (transformations.PAULI_X, states.ZERO, states.ONE),
        (transformations.PAULI_Y, states.PLUS, states.MINUS),
        (transformations.PAULI_Z, states.MINUS, states.PLUS),
    ],
)
def test_apply(a, b, expected):
    # given

    # when
    result = qmath.apply(a, b)

    # then
    assert np.array_equal(result, expected)


def test_apply_switched_throws():
    # given
    h = transformations.HADAMARD
    z = states.ZERO

    # when
    # then
    with pytest.raises(ValueError):
        qmath.apply(z, h)


def test_apply_empty_throws():
    # given
    h = []
    o = states.OO

    # when
    # then
    with pytest.raises(ValueError):
        qmath.apply(h, o)


def test_apply_dim_missmatch_throws():
    # given
    h = [1]
    o = states.OO

    # when
    # then
    with pytest.raises(ValueError):
        qmath.apply(h, o)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (np.array([1, 1]), np.array([1, -1]), np.array([1, -1, 1, -1])),
        (np.array([-1]), np.array([1, -1]), np.array([-1, 1])),
        (np.array([2]), np.array([4]), np.array([8])),
        (
            np.array([[1, 1], [-1, -1]]),
            np.array([1, -1]),
            np.array([[1, -1, 1, -1], [-1, 1, -1, 1]]),
        ),
    ],
)
def test_tensor_product(a, b, expected):
    # given

    # when
    result = qmath.tensor_product(a, b)

    # then
    assert np.array_equal(result, expected)


def test_tensor_product_wrong_type():
    # given
    a = 7
    b = np.array([8])

    # when
    result = qmath.tensor_product(a, b)

    # then
    assert np.array_equal(result, [56])


def test_tensor_product_empty():
    # given
    a = np.array([])
    b = np.array([])

    # when
    # then
    with pytest.raises(ValueError):
        qmath.tensor_product(a, b)


@pytest.mark.parametrize(
    "state,expected",
    [
        (np.array([]), math.sqrt(0)),
        (np.array([1]), math.sqrt(1)),
        (np.array([1, 1]), math.sqrt(2)),
        (np.array([1, 1, 1]), math.sqrt(3)),
        (np.array([1, 1, 1, 1]), math.sqrt(4)),
        (np.array([1, -1, -1, 1]), math.sqrt(4)),
        (np.array([[1], [1], [1], [1]]), math.sqrt(4)),
        (np.array([[1, 1], [1, 1]]), math.sqrt(4)),
    ],
)
def test_length(state, expected):
    # given
    # when
    result = qmath.length(state)
    # then
    assert result == expected


@pytest.mark.parametrize(
    "qbit,expected",
    [
        (states.PLUS, 45 / 180 * math.pi),
        (states.MINUS, 45 / 180 * math.pi),
        (states.ONE, 90 / 180 * math.pi),
        (states.ZERO, 0 / 180 * math.pi),
    ],
)
def test_calc_angle_to_zero(qbit, expected):
    # given
    # when
    result = qmath.calc_angle_to_zero(qbit)
    # then
    assert math.isclose(result, expected)


@pytest.mark.parametrize(
    "qbit,expected",
    [
        (np.array([1, 0, 0]), 0 / 180 * math.pi),
        (np.array([0, 1, 0]), 90 / 180 * math.pi),
        (np.array([0, 0, 1]), 90 / 180 * math.pi),
        (np.array([0]), 90 / 180 * math.pi),
        (np.array([0]), 90 / 180 * math.pi),
        (np.array([0]), 90 / 180 * math.pi),
        (np.array([0]), 90 / 180 * math.pi),
    ],
)
def test_calc_angle_to_zero_raises(qbit, expected):
    # given
    # when
    # then
    with pytest.raises(ValueError):
        qmath.calc_angle_to_zero(qbit)


@pytest.mark.parametrize(
    "qbit,expected",
    [(states.PLUS, 0.5), (states.MINUS, 0.5), (states.ONE, 0.0), (states.ZERO, 1.0)],
)
def test_calc_angle_to_zero(qbit, expected):
    # given
    # when
    result = qmath.prob_qbit_zero(qbit)
    # then
    assert math.isclose(result, expected)


@pytest.mark.parametrize(
    "state,expected",
    [(states.PP, 0.5), (states.MM, 0.5), (states.OO, 0.0), (states.ZZ, 1.0)],
)
def test_prob_first_digit_zero(state, expected):
    # given
    # when
    result = qmath.prob_first_digit_zero(state)
    # then
    assert math.isclose(result, expected)


def test_generate_bell_state():
    # given
    h = transformations.HADAMARD
    z = states.ZERO
    cnot = transformations.CNOT

    # when
    # generate bell state
    x = qmath.apply(h, z)
    x = qmath.tensor_product(x, z)
    bell = qmath.apply(cnot, x)

    # then
    assert np.array_equal(bell, states.BELL)
