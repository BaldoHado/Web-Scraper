import requests
from bs4 import BeautifulSoup, MarkupResemblesLocatorWarning


def get_summary(ticker):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
    }
    URL = f'https://finance.yahoo.com/quote/{ticker}?p={ticker}'
    page = requests.get(URL, headers=headers).content
    soup = BeautifulSoup(page, 'html.parser')
    # area_table = soup.select("table > tbody > td")
    area_data = soup.find_all("td")
    res = []
    for z in range(0, len(area_data) - 1, 2):
        res.append((f'{area_data[z].text}', f'{area_data[z + 1].text}'))
    return res


def existing_stock(ticker):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
    }
    URL = f'https://finance.yahoo.com/lookup?s={ticker}'
    page = requests.get(URL, headers=headers, allow_redirects=False)
    soup = BeautifulSoup(page.content, 'html.parser')
    area_data = soup.find_all("td")
    for k in area_data:
        if k.text == ticker:
            return True
    return False

