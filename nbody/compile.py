import cffi

ffi = cffi.FFI()
ffi.cdef("double nbody(unsigned int n);")

ffi.set_source(
    "_nbody",
    """
#include "nbody_1.h"
""",
    sources=["nbody_1.c"],
    libraries=["m"],
)
ffi.compile()
