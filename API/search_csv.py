import csv

class SearchCSV:
    def out_stuff(self):
        path = r'C:\Users\OXXO\Downloads\recommends.csv'
        with open(path) as csvfile :
            data = csv.reader(csvfile)
            for row in data:
                yield row

    def get(self, sku, sim=0):
        recoms = []
        sim = float(sim)
        for i in SearchCSV.out_stuff(self):
            if i[1]==sku and sim==0:
                recoms.append(i)
            elif i[1]==sku and sim>0:
                if float(i[2]) > sim:
                   recoms.append(i)

        return recoms


if __name__ == "__main__":
    INPUT = ['Ss01C6ny1O', 0.7]
    prod = product()
    rec_list = prod.get(INPUT[0], INPUT[1])
    print(rec_list)
