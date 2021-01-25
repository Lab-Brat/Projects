# Using Genetic Algorithm (GA) to simulate the 
# breeding process of Giant Spiders

import random

# Constants
GOAL = 6000
NUM_SPI = 50
INIT_MIN_W = 80
INIT_MAX_W = 200
INIT_MOD_W = 100
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

def select(population, to_retain):
    pop_s = sorted(population)
    retain_by_sex = to_retain//2
    members_per_sex = len(pop_s)//2

    # divide population by sex
    males = pop_s[:members_per_sex] #   0->25 (from smallest w to mid)
    females = pop_s[members_per_sex:] # 25->50 (form mid w to largest)
    selected_males = males[-retain_by_sex:] 
    selected_females = females[-retain_by_sex:] # select from end

    # print(retain_by_sex, members_per_sex)

    return selected_males, selected_females


pop = populate(NUM_SPI, INIT_MIN_W, INIT_MAX_W, INIT_MOD_W)
pop_fit = fitness(pop, GOAL)

sm, sf = select(pop, NUM_SPI)

print(sm, sf)