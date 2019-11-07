
import requests

for i in range(1000):
    r=requests.get('https://google.com')

print(r.text)