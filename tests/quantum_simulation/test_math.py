import numpy as np
import pytest
from quantum_simulation import math as qmath, apply, Transformations
from quantum_simulation import States


def test_apply_h_z():
    # given
    h = Transformations.HADAMARD
    z = States.ZERO
    expected = States.PLUS

    # when
    result = apply(h, z)

    # then
    assert np.array_equal(result, expected)


def test_apply_h_o():
    # given
    h = Transformations.HADAMARD
    o = States.ONE
    expected = States.MINUS

    # when
    result = apply(h, o)

    # then
    assert np.array_equal(result, expected)


def test_apply_hh_zz():
    # given
    h = Transformations.HH
    z = States.ZZ
    expected = States.PP

    # when
    result = apply(h, z)

    # then
    assert np.array_equal(result, expected)


def test_apply_hh_oo():
    # given
    h = Transformations.HH
    o = States.OO
    expected = States.MM

    # when
    result = apply(h, o)

    # then
    assert np.array_equal(result, expected)


def test_apply_switched_throws():
    # given
    h = Transformations.HADAMARD
    z = States.ZERO

    # when
    # then
    with pytest.raises(ValueError):
        apply(z, h)


def test_apply_empty_throws():
    # given
    h = []
    o = States.OO

    # when
    # then
    with pytest.raises(ValueError):
        apply(h, o)


def test_apply_dim_missmatch_throws():
    # given
    h = [1]
    o = States.OO

    # when
    # then
    with pytest.raises(ValueError):
        apply(h, o)


def test_generate_bell_state():
    # given
    h = Transformations.HADAMARD
    z = States.ZERO
    cnot = Transformations.CNOT

    # when
    # generate bell state
    x = apply(h, z)
    xy = qmath.tensor_product(x, z)
    bell = qmath.apply(cnot, xy)

    # then
    assert np.array_equal(bell, States.BELL)
