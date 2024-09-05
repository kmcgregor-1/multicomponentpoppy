import numpy as np
from main import MulticomponentPopulation

MultiPopulation = MulticomponentPopulation()
MultiPopulation.set_number_of_points(100)
events = MultiPopulation.multicomponent_init()

Multicomponentpopulation = MultiPopulation.build_multicomponent_pop(events)

MultiPopulation.write_to_json(Multicomponentpopulation, "./examples", "sample_pop")

print(Multicomponentpopulation)