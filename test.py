from parameters import Material, Structure, Parameters
import numpy as np
from core import Hamiltonian
tin = Material(148.0, 0.000618, 0.666666, 0.1)

struct = Structure(np.array([50]))
params = Parameters(tin, struct)
print(params.print_parameters())
ham = Hamiltonian(struct)

k = np.array([[1, 2], [3, 4], [5, 6]])
i = np.array([0, 1])

print(ham.spectrum(k, i))
print(i.shape)
print(i.T.shape)
