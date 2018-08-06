from libc.math cimport sqrt

# cdef extern from "math.h":
#     double sqrt(double)
def confidence(int ups, int n, float z=1.44):
    if n == 0:
        return 0
    cdef float phat = float(ups) / n
    return ((phat + z*z/(2*n) - z * sqrt(
            (phat*(1-phat)+z*z/(4*n))/n))/(1+z*z/n))

cdef float confidence2(int ups, int n, float z=1.44):
    return confidence(ups, n, z)
    
cpdef confidence3(int ups, int n, float z=1.44):
    return confidence2(ups, n, z)