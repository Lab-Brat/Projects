import random
from scipy.spatial.distance import euclidean as eu
from Data import dataPreProcess

class SA():
    def __init__(self):
        self.coords = dataPreProcess().getLocs()
        self.L = len(self.coords)
        self.all_locs = [i for i in range(self.L)]

    def dist(self, loc1, loc2):
        """ Euclidean distance between two locations. """
        return eu(self.coords[loc1], self.coords[loc2])

    def fitness(self, path):
        """ Fitness value (total distance) of the path. """
        fit = 0
        for i in range(self.L):
            fit += self.dist(path[i], path[(i+1)%self.L])
        return fit

    def greedy(self):
        """ Greedy algorithm to obtain an initial path. """
        visit_loc = random.choice(self.all_locs)
        path = [visit_loc]
        unvisit_loc = set(self.all_locs)
        unvisit_loc.remove(visit_loc)

        # find shortest path
        while unvisit_loc:
            next_loc = min(unvisit_loc, key=lambda x: self.dist(visit_loc, x))
            unvisit_loc.remove(next_loc)
            path.append(next_loc)
            visit_loc = next_loc

        return path, self.fitness(path)

if __name__ == "__main__":
    fin_path, fit = SA().greedy()
    print("Path:\n{0}\nTotal distance: {1:.2f}".format(fin_path, fit))
