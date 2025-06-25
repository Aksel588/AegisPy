# setup.py

from setuptools import setup

setup(
    name="aegispy",
    version="0.1",
    py_modules=["cli"],
    entry_points={
        'console_scripts': [
            'aegispy=cli:main',
        ],
    },
)