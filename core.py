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

    def __init__(self):
        self.spectrum = self.free_spectrum

    def free_spectrum(self, kx, ky, kz):
        """ Return the quadratic spectrum

        We implicitely assume any of the passed k's can be a discrete set
        of bands, though provided in the form (i+1)²pi²/L².
        """
        return h22m * (kx**2 + ky**2 + kz**2)


class System:
    ''' A system is responsible for calculating the superconducting properties.

    A system is defined by a Hamiltonian and a set of system parameters, and can
    calculate the superconducting properties from this. (Tc and Delta, and maybe
    more).
    '''

    def __init__(ham, par, struct):
        self.H = ham
        self.par = par
        self.struct = struct

    def overlaps():
        """ The interaction matrix elements.

        These are given by the wavefunction overlaps of the simple free-particle
        wavefunctions.
        At the moment, this is only implemented for 2D!
        """

        size = self.par.imax
        Lz = self.struct.dims[-1]
        return (np.ones(size, size) + np.identity(size, size))/Lz

    def getTc():
        phi = overlaps()
        integrator = Integrator(self.struct)
        kx, ky, kz = integrator.getkpoints()
        ksi = self.H.spectrum(kx, ky, kz)
