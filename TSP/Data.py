import random

# with open("locations.txt") as txt:
#     data = [loc for loc in txt]
#     txt.close()

data = [        [10,10], [15,30], [45,77],  [20,50],  [60,50],
                [60,15], [90,25], [90,79],  [54,18],  [21,10],
                [63,91], [16,71], [26,29],  [58,39],  [33,15],
                [33,55], [80,90], [100,79], [100,59], [22,80],
                [33,81], [48,88], [50,77],  [90,76],  [20,56],
                [80,60], [30,5],  [20,10],  [0,30],   [100,80],
                [11,54], [11,90], [11,18],  [80,43],  [43,81],
                [76,67], [57,50], [99,21],  [99,88],  [5,31]
        ]


ran_seq = random.sample(range(1,41), 40)

res1 = [5,10,15,20,25,30,35,40]     # only visit 3 of these
res2 = [2,4,6,8,10,20,22,32,33,35]  # only visit 5 of these

res1_sel = random.sample(res1, 3)
res2_sel = random.sample(res2, 5)

res_set = set(res1).union(set(res2))
res_sel_set = set(res1_sel).union(set(res2_sel))

fin_seq = [i for i in ran_seq if i not in res_set]
fin_seq.extend(res_sel_set)

print(sorted(fin_seq), len(fin_seq))
