import requests

BASE = 'http://127.0.0.1:5000/'

response = requests.get(BASE)
print(response.json())

# start server then run test.py