import subprocess
from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

ffiles = ['hello_fortran.f90']
libname = 'fmods'

FC = 'gfortran'
FFLAG = ('-c', '-fPIC', '-O3')


# compile all specified Fortran files to object codes
ofiles = []
for f in ffiles:
    ofile = f.split('.')[0] + '.o'
    ofiles.append(ofile)
    subprocess.run([FC, *FFLAG, f, '-o', ofile])

# link all object codes and put into a shared library
soname = 'lib' + libname + '.so'
res = subprocess.run([FC, *ofiles, '-shared', '-o', soname])


files = ['hello_cython.pyx']

ext_module = [Extension(
        name="myhello",
        sources=files,
        libraries=[libname],
        library_dirs=["."],
        include_dirs=["."],
        runtime_library_dirs=["."],
        extra_compile_args=["-O3"],
        )
        ]


setup(name="myhello",
        ext_modules=cythonize(ext_module, language_level=3),
        )
