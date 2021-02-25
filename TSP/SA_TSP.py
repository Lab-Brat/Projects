import random, math, copy, numpy
import matplotlib.pyplot as plt
from math import sqrt
from scipy.spatial import distance
from Data import dataPreProcess

# Importing Data
coords_list = dataPreProcess().getLocs()

############################## SIMULATED ANNEALING #######################################

# DEFINING THE ALGORITHM
def TSP_SA(data,n):

    customers = data.copy()
    #choosing random route
    route = random.sample(range(n),n)

    #THE ALGORITHM
    #setting up temperature, 200K in this case
    for temperature in numpy.logspace(0,5,num=200000)[::-1]:
        #make a new route by randomly swapping two customers in 'route'
        [i,j] = sorted(random.sample(range(n),2))
        new_Route =  route[:i] + route[j:j+1] +  route[i+1:j] + route[i:i+1] + route[j+1:]

        #fourmulas
        oldDistances =  sum([ math.sqrt(sum([(customers[route[(k+1) % n]][d] - customers[route[k % n]][d])**2 for d in [0,1] ])) for k in [j,j-1,i,i-1]])
        newDistances =  sum([ math.sqrt(sum([(customers[new_Route[(k+1) % n]][d] - customers[new_Route[k % n]][d])**2 for d in [0,1] ])) for k in [j,j-1,i,i-1]])

        #if if condition is satisfied, old route will be replace by new route
        if math.exp( ( oldDistances - newDistances) / temperature) > random.random():
            route = copy.copy(new_Route)


    #setting up parameters to plot the result
    xs = [customers[route[i % n]][0] for i in range(n+1)]
    ys = [customers[route[i % n]][1] for i in range(n+1)]

    total_dist = 0
    for k in range(len(xs)-1):
        total_dist += sqrt((xs[k] - xs[k+1])**2 + (ys[k] - ys[k+1])**2)

    plt.plot(xs, ys, 'ob-')
    plt.show()

    print("Total Distance: ", total_dist)
    print(customers)


TSP_SA(coords_list,len(coords_list))
