import requests

url = "https://api.adviceslip.com/advice"
response = requests.get(url)
data = response.json()

print(data["slip"]["advice"]) 