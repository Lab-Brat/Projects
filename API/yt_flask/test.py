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

# response = requests.get(BASE + "video/3")
# print(response.json())

data = [{"name": "Finding a job in IT", "views": 12345, "likes": 100},
        {"name": "How to cook bolognese", "views": 88888, "likes": 2000},
        {"name": "Otter eating sushi", "views": 9999999, "likes": 6000}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

response = requests.delete(BASE + 'video/1')
print(response)
input()
# get the rest
for i in range(2):
    response = requests.get(BASE + "video/" + str(i+1))
    print(response.json())
