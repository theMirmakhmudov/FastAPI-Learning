import requests

url = "http://127.0.0.1:8000/user_role/admin"

response = requests.get(url=url)

print(response.json())