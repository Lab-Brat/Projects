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

recoms = []
for i in out_stuff(path):
    if i[1] == 'Ss01C6ny1O':
        recoms.append(i)

end = time.time()
print("quantity of recommendaitons: ", len(recoms))
print('it took {0: .2f} seconds'.format(end-start))
