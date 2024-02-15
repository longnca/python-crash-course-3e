import requests
import json

url = 'https://hacker-news.firebaseio.com/v0/item/31353677.json'
r =requests.get(url)

print(r.status_code)
response_dict = r.json()
print(response_dict.keys())

response_string = json.dumps(response_dict, indent=4)
print(response_string)