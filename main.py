import platform
from timeit import timeit

import nbody._nbody as nbody_c
from nbody.nbody_2 import nbody as nbody_python

nbody_c = nbody_c.lib.nbody
n = 50000000


def calc_c(n=1):
    print(f"{nbody_c(1):.9f}")
    print(f"{nbody_c(n):.9f}")


def calc_python(n=1):
    print(f"{nbody_python(1):.9f}")
    print(f"{nbody_python(n):.9f}")


print(f"N-Body - Python {platform.python_version()} with C module")
print("Time:", timeit(f"calc_c({n})", number=1, setup="from __main__ import calc_c"))
print()

print(f"N-Body - Python {platform.python_version()}")
print(
    "Time:",
    timeit(f"calc_python({n})", number=1, setup="from __main__ import calc_python"),
)
