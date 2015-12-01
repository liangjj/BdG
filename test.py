from parameters import Material, Structure, Parameters, Integrator
import numpy as np
from core import Hamiltonian, System
tin = Material(148.0, 0.000618, 0.666666, 0.1)
Lz = 50.0

struct = Structure(np.array([Lz]))
params = Parameters(tin, struct)
print(params.print_parameters())
ham = Hamiltonian()
integrator = Integrator(struct)
sys = System(ham, params, struct)

print(integrator.integrate(ham.spectrum, [10, 10, 10]))
print(sys.getTc())
print(struct.cont_dims)
