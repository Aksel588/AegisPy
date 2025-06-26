# setup.py
#
# This file configures the packaging and installation of your Aegispy application.
# It uses setuptools for packaging and Cython for compiling Python modules.
#
# Usage:
#   python setup.py install
#
# This will install the package and make the 'aegispy' CLI available.
#
# You can customize this file to add dependencies, package data, or other modules as needed.
#
"""
Setup script for packaging and installing the Aegispy application.
Edit this file to configure package metadata, entry points, and Cython extensions.
"""

from setuptools import setup
from Cython.Build import cythonize

setup(
    name='aegispy',
    version='0.1',
    py_modules=['cli'],
    entry_points={
        'console_scripts': [
            'aegispy=cli:main',
        ],
    },
    ext_modules=cythonize(
        "template/core/secure_assets.py",
        compiler_directives={'language_level': "3"},
    ),
)