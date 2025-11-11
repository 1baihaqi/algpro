import requests

url = "http://127.0.0.1:5000/calculate/matrix"
data = {
    "matrix": [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]],
    "operation": "rank"
}

response = requests.post(url, json=data)
print(response.json())
