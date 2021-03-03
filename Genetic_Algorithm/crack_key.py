import time
import random
from itertools import product

class Crack_Code():
    def __init__(self, code_len, code_ints):
        self.code_len = code_len
        self.code_ints = code_ints
        self.combo = [random.choice(code_ints) for i in range(code_len)]
        self.N = len(self.combo)

    def brute_force(self):
        count = 0
        permutations = product(self.code_ints, repeat=code_len)
        print(self.combo)

        # find permutations with repetition to guess
        for p in permutations:
            if list(p) == self.combo:
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

        while attempt != self.combo:
            next_att = attempt[:]
            find_num = random.randint(0, self.N-1)
            next_att[find_num] = random.choice(self.code_ints)

            next_att_fit = self.fitness(next_att)
            if next_att_fit > attempt_fit:
                attempt = next_att[:]
                attempt_fit = next_att_fit
            count += 1

        print("Cracked!!!")
        print("The code was: {}".format(self.combo))
        print("It took {} tries".format(count))


if __name__ == '__main__':
    start = time.time()

    code_len = 7
    code_ints = [i for i in range(code_len)]
    model = Crack_Code(code_len, code_ints)
    # model.genetic_hill()
    model.brute_force()

    end = time.time()
    print("Runtime was {0:.2f} seconds.".format(end-start))
