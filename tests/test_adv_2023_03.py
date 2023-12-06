"""tests of adv_2023_03"""

import test_utils as tu
import solutions.adv_2023_03 as sol

_INPUTS = tu.get_all_inputs(3, {"small", "p"})

test_solve_a, test_solve_b = tu.get_solve_tests(
    sol.solve_a,
    {"small": 4361, "p": 525911},
    sol.solve_b,
    {"small": 467835, "p": 75805607},
    _INPUTS,
)
