from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("pypi_test_yomichi/fib.pyx")
)