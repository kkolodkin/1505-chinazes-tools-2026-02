import urllib.request
import urllib.parse
import json
import ssl

text = input("Введите текст на английском (до 200 символов): ")
params = urllib.parse.urlencode({"q": text, "langpair": "en|ru"})
url = f"https://api.mymemory.translated.net/get?{params}"

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
res = urllib.request.urlopen(req, context=ssl._create_unverified_context())
data = json.loads(res.read().decode('utf-8'))

print(data['responseData']['translatedText'])