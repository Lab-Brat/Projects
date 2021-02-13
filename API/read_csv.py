import time
import pandas as pd

# Download from Yandex Disk
# CSV_URL = 'https://disk.yandex.ru/d/13F2EVvW3zQ-Fw' # test csv file
CSV_URL = 'https://yadi.sk/d/NG-huzs-X-5U5Q'
DWN_URL = 'https://getfile.dokpub.com/yandex/get/' + CSV_URL

# Download From Google Drive
# CSV_URL = 'https://drive.google.com/file/d/1dYmMyb7EcMv5nV0Ak' + \
#           'Q4z_VuLtvBDrCIh/view?usp=sharing'
# FILE_ID = CSV_URL.split('/')[-2]
# DWN_URL ='https://drive.google.com/uc?export=download&id=' + FILE_ID

# url = requests.get(DWN_URL).text
# csv_raw = StringIO(url)
# dfs = pd.read_csv(csv_raw, chunksize=20, iterator=True)


# read from web
dfs = pd.read_csv(DWN_URL, header=None, chunksize=10, iterator=True)

# read from local download
start = time.time()
# path = r'C:\Users\OXXO\Downloads\recommends.csv'
# dfs = pd.read_csv(path, header=None, chunksize=100000, iterator=True)

for iter_num, chunk in enumerate(dfs, 1):
    print('one piece')
    print(iter_num, chunk)
    break

end = time.time()
print("Read Time: {}".format(end-start))
