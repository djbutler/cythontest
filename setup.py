# setup.py

from setuptools import setup, Extension
from Cython.Distutils import build_ext
#from Cython.Build import cythonize

cythonwrapper = Extension('cythonwrapper',
    sources = ['cythonwrapper.pyx', 'src/helloworld.cpp'],
    include_dirs = ['include/'],
    language = "c++")

setup(name='cythontestname',
      packages=['cythontest'],
      install_requires=['cython>=0.22'],
      ext_modules=[cythonwrapper],
      cmdclass = {'build_ext': build_ext})
