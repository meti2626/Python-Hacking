import requests

response = requests.get("https://www.scrapethissite.com/")

print(response.text)