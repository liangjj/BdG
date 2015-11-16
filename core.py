""" Module that contains core functionality.

Classes contained:
    - Hamiltonian: Initialized as a free particle Hamiltonian, which can return
    a 'Spectrum' or a 'Dos'. 'Corrections' can be applied to it, resulting in a
    modified 'Spectrum' and 'Dos'.

"""

import numpy as np
from constants import *
from parameters import Material, Structure, Parameters


class Hamiltonian:
    ''' A Hamiltonian governs the spectrum and dos of a system.

    Fields: - Spectrum (function)
            - Dos (function)
    '''

    def __init__(self, struc):
        Ls = struc.dims

        def free_spectrum(k, i):
            return h22m * (np.sum(k.T**2, 0) +
                           np.sum(((i.T + 1) * pi / Ls[None, :])**2, 0))

        self.spectrum = free_spectrum
