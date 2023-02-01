import requests
from bs4 import BeautifulSoup

url = "https://tijerascreek.quick18.com/teetimes/searchmatrix?teedate=20230129"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
print(soup.prettify())
