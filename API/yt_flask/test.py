import requests

# defining base URL (location of an API)
BASE = "http://127.0.0.1:5000/"

# response = requests.get(BASE + "testing/vasya")

# testing video request
# response = requests.put(BASE + "video/1", {"name": "Yara", \
#                                            "views": 12345, \
#                                            "likes": 100})
# print(response.json())
#
# # pause until enter is pressed
# input()
#
# for i in range(2):
#     response = requests.get(BASE + "video/" + str(i+1))
#     print(response.json())

response = requests.get(BASE + "video/2")
print(response.json())
