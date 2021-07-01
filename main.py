import requests
from bs4 import BeautifulSoup

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = 'https://www.amazon.in/dp/B0864JNFB8/ref=fs_a_ip_0'
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup.prettify())
    title = soup.find(id='productTitle')
    print(title.text.strip())
    price = soup.find(id='priceblock_ourprice')
    print(price)
