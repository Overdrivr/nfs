#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import nfs

setup(
    name='nfs',
    version=nfs.__version__,
    packages=find_packages(),
    author="Remi Beges",
    author_email="remi.beges@nxp.com",
    description="Processing utility for near-field scanners",
    long_description=open('README.md').read(),
    install_requires= ['docopt>=0.6.2', 'fastnumbers', 'numpy'],
    include_package_data=True,
    url='http://github.com/Overdrivr',
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers.
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: MIT License"
    ]
)
