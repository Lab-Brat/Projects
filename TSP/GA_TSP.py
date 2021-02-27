import math, random
import random
from sklearn.metrics.pairwise import pairwise_distances
from scipy.spatial.distance import euclidean as eu
from Data import dataPreProcess

class GA():
    def __init__(self):
        self.coords = dataPreProcess().getLocs()
        self.L = len(self.coords)
        self.genes = [i for i in range(self.L)]
        self.chrom = 300
        self.distances = pairwise_distances(self.coords, metric='euclidean')
        self.pop = [random.sample(self.genes, self.L) for i in range(self.chrom)]

    # def fitness(self, chromosome):
    #     fitness = 0
    #     xs = [self.coords[chromosome[i%self.L]][0] for i in range(self.L+1)]
    #     ys = [self.coords[chromosome[i%self.L]][1] for i in range(self.L+1)]
    #
    #     for k in range(len(xs)-1):
    #         fitness += math.sqrt((xs[k]-xs[k+1])**2 + (ys[k]-ys[k+1])**2)
    #
    #     return fitness

    def dist(self, loc1, loc2):
        """ Euclidean distance between two locations. """
        return eu(self.coords[loc1], self.coords[loc2])

    def fitness(self, path):
        """ Fitness value (total distance) of the path. """
        fit = 0
        for i in range(self.L):
            fit += self.dist(path[i%self.L], path[(i+1) % self.L])
        return fit

    def check(self):
        return (self.fitness(self.pop[10]))




if __name__ == "__main__":
    C = GA().check()
    print(C)
