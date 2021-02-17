import time
import requests
from pprint import pprint

# defining base URL (location of an API)
BASE = "http://127.0.0.1:5000/"
sku = 'Ss01C6ny1O'
sim = '0.7'

start = time.time()

response = requests.get(BASE + "prod/" + sku + "/" + sim)
pprint(response.json())

end = time.time()
print('it took {0:.2f} seconds'.format(end-start))
