from bs4 import BeautifulSoup
import requests

# page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
page = requests.get("https://jakelyell.dev/")
# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify)