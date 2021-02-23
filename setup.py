import subprocess
from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

ffiles = ['hello_fortran.f90']
libname = 'fmods'

FC = 'gfortran'
FFLAG = ('-c', '-fPIC', '-O3')


# compile all specified Fortran files to object codes
print('===================')
print('Generate object codes...')
ofiles = []
for f in ffiles:
    ofile = f.split('.')[0] + '.o'
    ofiles.append(ofile)
    res = subprocess.run([FC, *FFLAG, f, '-o', ofile])
    print(' '.join(res.args))
print('===================')

# link all object codes and put into a shared library
print('Create a shared library...')
soname = 'lib' + libname + '.so'
res = subprocess.run([FC, *ofiles, '-shared', '-o', soname])
print(' '.join(res.args))
print('===================')


# Cython wrapper
files = ['hello_cython.pyx']

# extension module object
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

# the setup command
print('Create the extension module...')
setup(name="myhello",
        ext_modules=cythonize(ext_module, language_level=3),
        )
print('===================')


# clean up manually
print('Clean up...')
cfiles = [f.split('.')[0] + '.c' for f in files]
subprocess.run(['rm', '-r', 'build/', *ofiles, *cfiles])
print('===================')
