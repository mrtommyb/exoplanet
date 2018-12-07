#!/usr/bin/env python

import numpy as np

import os
import sys
from setuptools import setup

dirname = os.path.dirname(os.path.realpath(__file__))
sys.insert(0, os.path.join(dirname, "exoplanet"))
from exoplanet_version import __version__


with open(os.path.join(dirname, "requirements.txt"), "r") as f:
    install_requires = f.read().splitlines()


with open(os.path.join(dirname, "README.rst"), encoding="utf-8") as f:
    readme = f.read()


setup(
    name="exoplanet",
    version=__version__,
    author="Daniel Foreman-Mackey",
    author_email="foreman.mackey@gmail.com",
    url="https://github.com/dfm/exoplanet",
    license="MIT",
    packages=[
        "exoplanet",
        "exoplanet.gp",
        "exoplanet.orbits",
        "exoplanet.theano_ops",
        "exoplanet.theano_ops.starry",
        "exoplanet.theano_ops.kepler",
        "exoplanet.theano_ops.celerite",
    ],
    description="Fast & scalable MCMC for all your exoplanet needs",
    long_description=readme,
    install_requires=install_requires,
    package_data={"": ["README.rst", "LICENSE"]},
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    zip_safe=True,
)
