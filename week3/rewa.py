import requests
import re

url =  "https://www.scrapethissite.com/"

response = requests.get(url)
html = response.text



populations = re.findall(r'\d{3,}', html)

for pop in populations:
    print("📊 Population found:", pop)