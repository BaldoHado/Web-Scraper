import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
}

URL = "https://finance.yahoo.com/quote/AMD/key-statistics?p=AMD"
page = requests.get(URL, headers=headers).content

soup = BeautifulSoup(page, 'html.parser')

#area_headers = soup.select("tbody > tr > td > span")

area_data = soup.select("tbody > tr > td")

area_headers = soup.select("div > h3 > span")

#res = area.find_all("span")


for z in area_data:
    print(z.text)
