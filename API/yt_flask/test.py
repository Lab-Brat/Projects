import requests

# defining base URL (location of an API)
BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "testing")
print(response.json())
