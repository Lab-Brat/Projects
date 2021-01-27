import time 
import random
from itertools import product

def brute_force(combo):
    # combo = (9,9,7,6,5,4,3)
    count = 0
    nums = [0,1,2,3,4,5,6,7,8,9]
    permutations = product(nums, repeat=len(combo))

    # find permutations with repetition to guess 
    for p in permutations:
        if p == combo:
            print("Cracked!!!")
            print("The code was: {}".format(combo))
            print("It took {} tries".format(count))
        else:
            count += 1

def main():
    combo = []
    for i in range(7):
        combo.append(random.randint(0, 9))
    combo_t = tuple(combo)

    brute_force(combo_t)


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print("Runtime was {0:.2f} seconds.".format(duration))