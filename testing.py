import requests

url = "https://www.google.de"
response = requests.get(url)

print(response.status_code)
print(response.text)
