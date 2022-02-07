import requests

# url = "https://www.python.org/"
# response = requests.get(url)
# print(response)
# print(response.request)
# print(response.request.headers)
# print(response.status_code)
# print(response.reason)
# print(response.headers)
# print(response.text)

# downloading a image with requests library
url = "https://www.python.org/static/img/python-logo.png"
response = requests.get(url)
with open('python.jpg', 'wb') as r:
    r.write(response.content)