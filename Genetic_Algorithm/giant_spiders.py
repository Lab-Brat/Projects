# Using Genetic Algorithm (GA) to simulate the 
# breeding process of Giant Spiders

import time
import random


# Constants
GOAL = 10000
NUM_SPI = 50
INIT_MIN_W = 80
INIT_MAX_W = 200
INIT_MOD_W = 100
MUTATE_ODDS = 0.1
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


def breed(males, females, hatch_num):
    random.shuffle(males)
    random.shuffle(females)
    children = []

    for male, female in zip(males, females): # group by two (crossover)
        for child in range(hatch_num):
            child = random.randint(male, female)
            children.append(child)
        
    return children


def mutate(children, mutate_odds, mutate_min, mutate_max):
    for index, rat in enumerate(children):
        if mutate_odds >= random.random():
            children[index] = round(rat*random.uniform(mutate_min, mutate_max))
    return children

# Genetic Algorithm
def main():
    generations = 0

    # initialize population
    parents = populate(NUM_SPI, INIT_MIN_W, INIT_MAX_W,INIT_MOD_W)
    print("initial population weights = {}".format(parents))

    # calculate population fitness
    pop_fit = fitness(parents, GOAL)
    print("initial population fitness = {}".format(pop_fit))
    print("number to retain = {}".format(NUM_SPI))

    ave_wt = []

    while pop_fit < 1 and generations < LIMIT:
        # split by sex
        selected_males, selected_females = select(parents, NUM_SPI)

        # crossover and mutation
        children = breed(selected_males, selected_females, HATCH_NUM)
        children = mutate(children, MUTATE_ODDS, MUTATE_MIN, MUTATE_MAX)

        # add everything together, recalculate fitness
        parents = selected_males + selected_females + children
        pop_fit = fitness(parents, GOAL)
        print("Generation {} fitness = {:.4f}".format(generations, pop_fit))
        ave_wt.append(int(mean(parents)))
        generations += 1

    # output information
    print("average weight per generation = {}".format(ave_wt))
    print("\nnumber of generations = {}".format(generations))
    print("number of years = {}".format(int(generations / PER_YEAR)))

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print("\nRuntime for this program was {} seconds.".format(duration))    