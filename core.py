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
        self.spectrum = self.free_spectrum


    def free_spectrum(kx, ky, kz):
        """ Return the quadratic spectrum

        We implicitely assume any of the passed k's can be a discrete set
        of bands, though provided in the form (i+1)²pi²/L².
        """
        return h22m * (kx**2 + ky**2 + kz**2)

    def dos(self, struc):
        n = struc.ndim

        return  
