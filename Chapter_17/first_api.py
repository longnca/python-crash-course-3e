import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print(f"Status code: {response.status_code}")
print(f"Complete response: {response.json()}")