import time
import random
from itertools import product

class Crack_Code():
    def __init__(self, code_len, code_ints):
        self.code_len = code_len
        self.code_ints = code_ints
        self.combo = [random.choice(code_ints) for i in range(code_len)]
        self.N = len(self.combo)
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

    def fitness(self, attempt):
        similarity = 0
        for i,j in zip(self.combo, attempt):
            if i==j:
                similarity += 1
        return similarity

    def genetic_hill(self):
        count = 0
        attempt = [0]*self.N
        attempt_fit = self.fitness(attempt)
        print(self.combo)

        while attempt != self.combo:
            next_att = attempt[:]
            find_num = random.randint(0, self.N-1)
            next_att[find_num] = random.sample(self.nums,1)[0]

            next_att_fit = self.fitness(next_att)
            if next_att_fit > attempt_fit:
                attempt = next_att[:]
                attempt_fit = next_att_fit
            print(next_att, attempt)
            count += 1

        print()
        print("Cracked!!!")
        print("The code was: {}".format(self.combo))
        print("It took {} tries".format(count))


if __name__ == '__main__':
    start = time.time()

    # combo_t = tuple([random.randint(0,9) for i in range(10)])
    code_len = 10
    code_ints = [i for i in range(10)]
    Crack_Code(code_len, code_ints).genetic_hill()

    end = time.time()
    print("Runtime was {0:.2f} seconds.".format(end-start))
