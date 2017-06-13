import requests
from bs4 import BeautifulSoup
import time
import pymongo

client=pymongo.MongoClient('localhost',27017)
second=client['xiao_zhu']
hz=second['hz']

def get_page_info(url):
    web_data=requests.get(url)
    time.sleep(2)
    soup=BeautifulSoup(web_data.text,'lxml')
    titles=soup.select('div.list > ul > li > div > p.infoBox > a')
    images=soup.select('div.list > ul > li > div > a > img')
    prices=soup.select('div.list > ul > li > div > p.priType-s > span > i')
    for title,image,price in zip(titles,images,prices):
        info={
            'title':title.get_text(),
            'image':image.get('src'),
            'price':price.get_text().replace(u'万', '').replace(' ', '')
        }
        hz.insert_one(info)
        print(info)
def get_totalPage_info():
    urls=["https://www.guazi.com/cd/buy/o{}/".format(str(i)) for i in range(1,382,1)]
    for url in urls:
        get_page_info(url)
if __name__ == '__main__':
    get_totalPage_info()