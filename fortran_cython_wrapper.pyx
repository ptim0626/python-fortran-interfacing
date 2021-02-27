cdef extern:
    void hello_fortran()
    void c_num_addition(int* a, double* b, double* ans)
    double complex c_cplxdiv(double complex* u, double complex* v)

def hello_world():
    hello_fortran()

def num_add(int a, double b):
    cdef double val=0
    c_num_addition(&a, &b, &val)
    return val

def complex_divide(double complex w1, double complex w2):
    cdef double complex val=0
    val = c_cplxdiv(&w1, &w2)
    return val

