from parameters import Material, Structure, Parameters
import numpy as np
tin = Material(148.0, 0.000618, 0.666666, 0.1)

struct = Structure(np.array([50]))
params = Parameters(tin, struct)
print(params.print_parameters())
