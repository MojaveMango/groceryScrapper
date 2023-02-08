import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
    url = 'https://giantfood.com/product/horizon-organic-milk-2-reduced-fat-1-2-gallon/90689'
    r = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(r.content, 'html.parser')
    price = soup.select_one('.pdl-product-detail_price-info > div:nth-child(1) > span:nth-child(1)')
    print(soup)