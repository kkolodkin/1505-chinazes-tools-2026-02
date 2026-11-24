import requests
url = 'https://api.quotable.io/random'
response = requests.gt(url)
data = response.json
print(data['content'])
print('-',data['author'])
