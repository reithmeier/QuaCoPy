import numpy as np

from quantum_simulation import math as qmath, apply
from quantum_simulation import Constants


def test_generate_bell_state():
    # given
    h = Constants.HADAMARD
    z = Constants.ZERO
    cnot = Constants.CNOT

    # when
    # generate bell state
    x = apply(h, z)
    xy = qmath.tensor_product(x, z)
    bell = qmath.apply(cnot, xy)

    # then
    assert np.array_equal(bell, Constants.BELL)
