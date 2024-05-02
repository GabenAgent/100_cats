import json
import requests


# from urllib import parse, request
#
# url = "http://api.giphy.com/v1/gifs/search"
# api_key = "EIkGxAqymsKn4iwsrA9CbV8y7n1WDAyW"
# content = input("Enter GIF theme please : ")
#
# params = parse.urlencode({
#     "q": content,
#     "api_key": api_key,
#     "limit": "5"
# })
#
# with request.urlopen("".join((url, "?", params))) as response:
#     data = json.loads(response.read())
#
# print(json.dumps(data, sort_keys=True, indent=4))


url = "http://api.giphy.com/v1/gifs/search"
api_key = "EIkGxAqymsKn4iwsrA9CbV8y7n1WDAyW"
content = input("Enter GIF theme please: ")

params = {
    "q": content,
    "api_key": api_key,
    "limit": "1"
}

response = requests.get(url, params=params)
print(response.json())
