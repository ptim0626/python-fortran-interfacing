cdef extern:
    void hello_fortran()

def hello_cython():
    print("Cython...")
    hello_fortran()
