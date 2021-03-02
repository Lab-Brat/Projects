import random
import matplotlib.pyplot as plt

# with open("locations.txt") as txt:
#     data = [loc for loc in txt]
#     txt.close()

# custromers locations
data = [        [10,10], [15,30], [45,77],  [20,50],  [60,50],
                [60,15], [90,25], [90,79],  [54,18],  [21,10],
                [63,91], [16,71], [26,29],  [58,39],  [33,15],
                [33,55], [80,90], [100,79], [100,59], [22,80],
                [33,81], [48,88], [50,77],  [90,76],  [20,56],
                [80,60], [30,5],  [20,10],  [0,30],   [100,80],
                [11,54], [11,90], [11,18],  [80,43],  [43,81],
                [76,67], [57,50], [99,21],  [99,88],  [5,31]
        ]

# visiting restrictions
res1 = [5,10,15,20,25,30,35,40]     # only visit 3 of these
res2 = [2,4,6,8,10,20,22,32,33,35]  # only visit 5 of these


class dataPreProcess():
    def __init__(self):
        self.data = data
        self.ran_seq = random.sample(range(1,len(data)+1), len(data))
        self.res1 = res1
        self.res2 = res2

    def getInds(self):
        '''Select locations to visit and output their indices'''
        # visit at least 3 locations from res1, and 5 from res2
        res1_sel = random.sample(self.res1, 3)
        res2_sel = random.sample(self.res2, 5)

        # select unique locations
        res_set = set(res1).union(set(res2))
        res_sel_set = set(res1_sel).union(set(res2_sel))

        # remove all restricted locations, then add the selected ones
        fin_seq = [i for i in self.ran_seq if i not in res_set]
        fin_seq.extend(res_sel_set)
        return fin_seq

    def getLocs(self):
        ''' Output actual locations from data using selected locations '''
        # sort indices, then use them to find locations in data
        coords_indx_sort = sorted(self.getInds())
        coords_list = [self.data[i-1] for i in coords_indx_sort]

        # start and finish at the depot coordinate
        depot = [0,0]
        coords_list.insert(0, depot)
        coords_list.append(depot)

        return coords_list

    def plotPath(self, coords, path, N):
        xs = [coords[path[i]][0] for i in range(N+1)]
        ys = [coords[path[i]][1] for i in range(N+1)]
        plt.plot(xs, ys, 'ob-')
        plt.show()

    def plot2Path(self, coords, path1, path2, N):
        xs1 = [coords[path1[i]][0] for i in range(N+1)]
        ys1 = [coords[path1[i]][1] for i in range(N+1)]
        xs2 = [coords[path2[i]][0] for i in range(N+1)]
        ys2 = [coords[path2[i]][1] for i in range(N+1)]

        fig, axs = plt.subplots(1, 2)
        fig.suptitle('Shortest paths by GA(left) and SA(right)')
        axs[0].plot(xs1, ys1)
        axs[1].plot(xs2, ys2)
        plt.show()

if __name__ == '__main__':
    LOC = dataPreProcess().getLocs()
    print(LOC)
