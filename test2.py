import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes":78, "name": "lucas", "views":100000},
        {"likes":323, "name": "blah", "views":1453434000},
        {"likes":676, "name": "jack", "views":9}]


for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()

response = requests.delete(BASE + "video/0")
print(response)

input()

response = requests.get(BASE + "video/2")
print(response.json())