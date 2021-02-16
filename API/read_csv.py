import csv
import time

# Download from Yandex Disk
# CSV_URL = 'https://yadi.sk/d/NG-huzs-X-5U5Q'
# DWN_URL = 'https://getfile.dokpub.com/yandex/get/' + CSV_URL

path = r'C:\Users\OXXO\Downloads\recommends.csv'

def out_stuff(path):
    with open(path) as csvfile :
        data = csv.reader(csvfile)
        for row in data:
            yield row

start = time.time()

def get_recoms(sku, threshold=0):
    recoms = []
    for i in out_stuff(path):
        if i[1]==sku and threshold==0:
            recoms.append(i)
        elif i[1]==sku and threshold>0:
            if float(i[2]) > threshold:
                recoms.append(i)
    return recoms

sku = 'Ss01C6ny1O'
# sku = 'WOaFaund0j'
recoms = get_recoms(sku, threshold=0.7)

end = time.time()
print("there are {} recommendaitons for {}: ".format(sku,len(recoms)))
print('it took {0: .2f} seconds'.format(end-start))
