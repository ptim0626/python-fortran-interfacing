import subprocess
import glob
from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

# the name of the extension module (imported by Python)
modname = 'fextension'
# all the Fortran files to be included in the extension module
ffiles = ['hello_fortran.f90', 'number_example.f90']
# Cython wrapper
sources = ['fortran_cython_wrapper.pyx']

# compiler and compiler flags for Fortran
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

# extension module object
ext_module = [Extension(
        name=modname,
        sources=sources,
        libraries=['gfortran'], # provide symbols used in Fortran during linking
        include_dirs=["."], # additional header directory
        extra_compile_args=['-O3', '-fPIC'],
        extra_objects=ofiles, # link all object files created by Fortran
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
module_files = glob.glob('*.mod')
subprocess.run(['rm', '-r', 'build/', *ofiles, *cfiles, *module_files])
print('===================')

