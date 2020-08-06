# -*- coding: utf-8 -*-

__all__ = [
    "__version__",
    "distributions",
    "gp",
    "orbits",
    "interp",
    "get_dense_nuts_step",
    "sample",
    "optimize",
]

from . import distributions, gp, interp, orbits
from .citations import CITATIONS
from .distributions import *  # NOQA
from .estimators import *  # NOQA
from .exoplanet_version import __version__
from .light_curves import *  # NOQA
from .optim import optimize
from .sampling import get_dense_nuts_step, sample
from .utils import *  # NOQA

__bibtex__ = __citation__ = CITATIONS["exoplanet"][1]
__uri__ = "https://docs.exoplanet.codes"
__author__ = "Daniel Foreman-Mackey"
__email__ = "foreman.mackey@gmail.com"
__license__ = "MIT"
__description__ = "Fast and scalable MCMC for all your exoplanet needs"
