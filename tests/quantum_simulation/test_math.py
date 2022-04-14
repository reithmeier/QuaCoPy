import numpy as np
import pytest
from quantum_simulation import math as qmath, apply, transformations
from quantum_simulation.constants import states


def test_apply_h_z():
    # given
    h = transformations.HADAMARD
    z = states.ZERO
    expected = states.PLUS

    # when
    result = apply(h, z)

    # then
    assert np.array_equal(result, expected)


def test_apply_h_o():
    # given
    h = transformations.HADAMARD
    o = states.ONE
    expected = states.MINUS

    # when
    result = apply(h, o)

    # then
    assert np.array_equal(result, expected)


def test_apply_hh_zz():
    # given
    h = transformations.HH
    z = states.ZZ
    expected = states.PP

    # when
    result = apply(h, z)

    # then
    assert np.array_equal(result, expected)


def test_apply_hh_oo():
    # given
    h = transformations.HH
    o = states.OO
    expected = states.MM

    # when
    result = apply(h, o)

    # then
    assert np.array_equal(result, expected)


def test_apply_switched_throws():
    # given
    h = transformations.HADAMARD
    z = states.ZERO

    # when
    # then
    with pytest.raises(ValueError):
        apply(z, h)


def test_apply_empty_throws():
    # given
    h = []
    o = states.OO

    # when
    # then
    with pytest.raises(ValueError):
        apply(h, o)


def test_apply_dim_missmatch_throws():
    # given
    h = [1]
    o = states.OO

    # when
    # then
    with pytest.raises(ValueError):
        apply(h, o)


def test_generate_bell_state():
    # given
    h = transformations.HADAMARD
    z = states.ZERO
    cnot = transformations.CNOT

    # when
    # generate bell state
    x = apply(h, z)
    xy = qmath.tensor_product(x, z)
    bell = qmath.apply(cnot, xy)

    # then
    assert np.array_equal(bell, states.BELL)
