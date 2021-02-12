import requests

# defining base URL (location of an API)
BASE = "http://127.0.0.1:5000/"

data = [{"name": "Finding a job in IT", "views": 12345, "likes": 100},
        {"name": "How to cook bolognese", "views": 88888, "likes": 2000},
        {"name": "Otter eating sushi", "views": 9999999, "likes": 6000}]

# put 3 videos into videos
for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

# delete 2nd video
response = requests.delete(BASE + 'video/1')
print(response)

# wait, continue after pressing 'enter'
input()

# output everything that's left
for i in range(2):
    response = requests.get(BASE + "video/" + str(i+1))
    print(response.json())
