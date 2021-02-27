import random
from scipy.spatial.distance import euclidean as eu
from Data import dataPreProcess


coords = dataPreProcess().getLocs()

def dist(loc1, loc2):
    """ Euclidean distance between two locations. """
    return eu(coords[loc1], coords[loc2])

def fitness(path):
    """ Fitness value (total distance) of the path. """
    fit = 0
    for i in range(len(coords)):
        fit += dist(path[i], path[(i+1)%len(coords)])
    return fit


def greedy():
    """ Greedy algorithm to obtain an initial path. """
    all_locs = [i for i in range(len(coords))]
    visit_loc = random.choice(all_locs)
    path = [visit_loc]
    unvisit_loc = set(all_locs)
    unvisit_loc.remove(visit_loc)

    # find shortest path
    while unvisit_loc:
        next_loc = min(unvisit_loc, key=lambda x: dist(visit_loc, x))
        unvisit_loc.remove(next_loc)
        path.append(next_loc)
        visit_loc = next_loc

    return path, fitness(path)

fin_path, fit = greedy()
print("Path: {0}\nTotal distance: {1:.2f}".format(fin_path, fit))
