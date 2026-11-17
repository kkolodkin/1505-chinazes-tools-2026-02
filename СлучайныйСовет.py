import urllib.request
import json
import ssl
import time

req = urllib.request.Request(f"https://api.adviceslip.com/advice?t={time.time()}", headers={'User-Agent': 'Mozilla/5.0'})
res = urllib.request.urlopen(req, context=ssl._create_unverified_context())
print(json.loads(res.read())['slip']['advice'])