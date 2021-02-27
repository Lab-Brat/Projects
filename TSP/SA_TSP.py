import random, math
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean as eu
from Data import dataPreProcess


coords = dataPreProcess().getLocs()
path = [i for i in range(len(coords))]
random.shuffle(path)

def dist(loc1, loc2):
    """ Euclidean distance between two nodes. """
    return eu(coords[loc1], coords[loc2])

def fitness(path):
    """ Total distance of the current path. """
    fit = 0
    for i in range(len(coords)):
        fit += dist(path[i], path[(i+1)%len(coords)])
    return fit

fit = fitness(path)
print(fit)
