import requests
from bs4 import BeautifulSoup

# Step 1: Go to the website
url = "https://www.scrapethissite.com/pages/simple/"
response = requests.get(url)

# Step 2: Parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Find each country block
countries = soup.find_all("div", class_="col-md-4 country")

# Step 4: Loop and print name + population
for country in countries:
    name = country.find("h3", class_="country-name").text.strip()
    population = country.find("span", class_="country-population").text.strip()
    print(f"🌍 {name} - Population: {population}")
