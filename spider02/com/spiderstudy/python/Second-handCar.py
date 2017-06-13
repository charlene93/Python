from bs4 import BeautifulSoup
import requests

def detailOper(url):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text, 'lxml')
    titles = soup.select('div.list > ul > li > div > p.infoBox > a')
    prices = soup.select('div.list > ul > li > div > p.priType-s > span > i')
    for title, price in zip(titles, prices):
        data = {
            'title': title.get_text(),
            'detailHerf': title.get('href'),
            'price':price.get_text().replace(u'万', '').replace(' ', '')
        }
        print(data)

def start():
    urls = ['http://www.guazi.com/tj/buy/o{}/'.format(str(i)) for i in range(1, 30, 1)]
    for url in urls:
        detailOper(url)

if __name__ == '__main__':
    start()