import requests

url = ""
response = requests.get(url)
weatherJSON = response.json()