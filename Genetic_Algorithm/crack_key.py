import time
import random
from itertools import product

class Crack_Code():
    def __init__(self, combo):
        self.combo = combo
        self.N = len(combo)
        self.nums = [i for i in range(10)]

    def brute_force(self):
        count = 0
        permutations = product(self.nums, repeat=self.N)

        # find permutations with repetition to guess
        for p in permutations:
            if p == self.combo:
                print("Cracked!!!")
                print("The code was: {}".format(self.combo))
                print("It took {} tries".format(count))
            else:
                count += 1


if __name__ == '__main__':
    start = time.time()

    combo_t = tuple([random.randint(0,9) for i in range(7)])
    Crack_Code(combo_t).brute_force()

    end = time.time()
    print("Runtime was {0:.2f} seconds.".format(end-start))
