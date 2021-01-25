# Using Genetic Algorithm (GA) to simulate the 
# breeding process of Giant Spiders

import random

# Constants
GOAL = 10000
NUM_SPI = 50
INIT_MIN_W = 80
INIT_MAX_W = 400
INIT_MOD_W = 200
MUTATE = 0.1
MUTATE_MIN = 0.8
MUTATE_MAX = 1.5
HATCH_NUM = 100
PER_YEAR = 5
LIMIT = 2000


def populate(num_spi, min_w, max_w, mode_w):
    return [int(random.triangular(min_w, max_w, mode_w)) for i in range(num_spi)]

def mean(lis):
    return sum(lis)/len(lis)

def fitness(population, goal):
    return mean(population)/goal

pop = populate(NUM_SPI, INIT_MIN_W, INIT_MAX_W, INIT_MOD_W)
M = mean(pop)
FIT = fitness(pop, GOAL)

print(M)