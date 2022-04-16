"""
Quantum States
"""
import math

import numpy as np

Z = ZERO = np.array([1, 0]).reshape((2, 1))
"""
|0> zero state
"""

O = ONE = np.array([0, 1]).reshape((2, 1))
"""
|1> one state
"""

ZZ = ZERO_ZERO = np.array([1, 0, 0, 0]).reshape((4, 1))
"""
|00> state
"""

ZO = ZERO_ONE = np.array([0, 1, 0, 0]).reshape((4, 1))
"""
|01> state
"""

OZ = ONE_ZERO = np.array([0, 0, 1, 0]).reshape((4, 1))
"""
|10> state
"""

OO = ONE_ONE = np.array([0, 0, 0, 1]).reshape((4, 1))
"""
|11> State
"""

P = PLUS = np.array([1 / math.sqrt(2), 1 / math.sqrt(2)]).reshape((2, 1))
"""
|+> plus state
"""

M = MINUS = np.array([1 / math.sqrt(2), -1 / math.sqrt(2)]).reshape((2, 1))
"""
|-> minus state
"""

PP = PLUS_PLUS = 1 / 2 * np.array([1, 1, 1, 1]).reshape((4, 1))
"""
|++> state
"""

PM = PLUS_MINUS = 1 / 2 * np.array([1, -1, 1, -1]).reshape((4, 1))
"""
|+-> state
"""

MP = MINUS_PLUS = 1 / 2 * np.array([-1, 1, -1, 1]).reshape((4, 1))
"""
|-+> state
"""

MM = MINUS_MINUS = 1 / 2 * np.array([1, -1, -1, 1]).reshape((4, 1))
"""
|--> state
"""

B = BELL = np.array([1 / math.sqrt(2), 0, 0, 1 / math.sqrt(2)]).reshape((4, 1))
"""
Bell state
"""
