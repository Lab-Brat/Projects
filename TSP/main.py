from Data import dataPreProcess
from GA_TSP import GA
from SA_TSP import SA

coords = dataPreProcess().getLocs()

print("---------  GA Starts  ---------")
GA = GA(coords, 250)
path_ga, path_fit_ga = GA.genetic()
print("GA Total Distance: ", path_fit_ga)

SA = SA(coords)
path_sa, path_fit_sa = SA.sim_anneal()
print("SA Total Distance: ", path_fit_sa)
