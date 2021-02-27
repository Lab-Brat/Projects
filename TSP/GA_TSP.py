import math, random
import random
from sklearn.metrics.pairwise import pairwise_distances
from Data import dataPreProcess

class GA():
    def __init__(self):
        self.coords = dataPreProcess().getLocs()

        self.genes = len(self.coords)
        self.chrom = 300
        self.distances = pairwise_distances(self.coords, metric='euclidean')
        self.pop = [random.sample(self.coords, self.genes) for i in range(self.chrom)]

    def check(self):
        return (len(self.pop), len(self.pop[33]), self.genes)




if __name__ == "__main__":
    C = GA().check()
    print(C)
