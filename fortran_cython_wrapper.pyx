cdef extern:
    # provide the C interface
    void c_hello_world()
    void c_num_addition(int* a, double* b, double* ans)
    void c_num_multi(double a, double b, double* ans)
    void c_num_plus1(float* a)
    double complex c_cplxdiv(double complex* u, double complex* v)

def hello_world():
    # no argument
    c_hello_world()

def num_add(int a, double b):
    # pass by reference
    cdef double val=0

    c_num_addition(&a, &b, &val)

    return val

def num_multi(double a, double b):
    # pass by copy
    cdef double val=0

    c_num_multi(a, b, &val)

    return val

def num_plus1(float a):
    # in-place operation

    c_num_plus1(&a)

    return a

def complex_divide(double complex w1, double complex w2):
    # a python/fortran function

    val = c_cplxdiv(&w1, &w2)

    return val

