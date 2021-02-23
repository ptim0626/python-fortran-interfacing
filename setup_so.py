import subprocess
from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

# the name of the extension module (imported by Python)
modname = 'myhello'
# all the Fortran files to be included in the extension module
ffiles = ['hello_fortran.f90']
# the external library path/name to include all object codes created
libname = 'fmods'
# Cython wrapper
sources = ['hello_cython.pyx']

# compiler and comipler flags for Fortran
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

# extension module object
ext_module = [Extension(
        name=modname,
        sources=sources,
        libraries=[libname], # the external library path
        library_dirs=['.'], # additional library directory to be searched
        include_dirs=['.'], # additional header directory
        runtime_library_dirs=['.'], # the path to 'libname', used in runtime
        extra_compile_args=['-O3', '-fPIC'],
        )
        ]

# the setup command
print('Create the extension module...')
setup(name=modname,
      ext_modules=cythonize(ext_module, language_level=3),
      )
print('===================')

# clean up manually
print('Clean up...')
cfiles = [f.split('.')[0] + '.c' for f in sources]
subprocess.run(['rm', '-r', 'build/', *ofiles, *cfiles])
print('===================')

