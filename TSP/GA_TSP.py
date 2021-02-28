import math, random
import random
from sklearn.metrics.pairwise import pairwise_distances
from scipy.spatial.distance import euclidean as eu
from Data import dataPreProcess

class GA():
    def __init__(self, population_size, selection_factor):
        self.coords = dataPreProcess().getLocs()
        self.L = len(self.coords)
        self.genes = [i for i in range(self.L)]
        self.chrom = population_size
        self.factor = selection_factor
        self.distances = pairwise_distances(self.coords, metric='euclidean')
        self.pop = [random.sample(self.genes, self.L) for i in range(self.chrom)]
        self.pop_sum = []
        self.new_pop = []

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
            fit += self.dist(path[i%self.L], path[(i+1)%self.L])
        return fit

    def selection(self, p=[1,0]):
        """ Stohastic universal sampling """
        total_fitness = sum([self.fitness(x) for x in self.pop])

        for x in self.pop:
            prob1 = (p[0]*(total_fitness - self.fitness(x))+p[1])
            prob2 = (p[0]*(total_fitness*(len(self.pop)-1))+p[1])
            prob = prob1/prob2
            self.pop_sum.append([x, prob])

        self.pop_sum.sort(key=lambda x:x[1])
        for i in range(1, len(self.pop_sum)):
            self.pop_sum[i][1] += self.pop_sum[i-1][1]

        r = random.random()
        for i in range(self.factor):
            sel_chrom = [x for x in self.pop_sum if x[1] >= (r+i/self.factor)%1][0]
            self.new_pop.append(sel_chrom)

        return self.new_pop

    def crossover(self):
        cp1, cp2 = random.sample(range(self.L), 2)
        if (cp1 > cp2):
            tmp = cp1
            cp1 = cp2
            cp2 = tmp

        return (cp1, cp2)



if __name__ == "__main__":
    cp1,cp2 = GA(300, 150).crossover()
    print(cp1,cp2)
