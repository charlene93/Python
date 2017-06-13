# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import csv

url="https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html"
urls=["https://www.tripadvisor.cn/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#ATTRACTION_LIST".format(str(x)) for x in range(30,1110,30)]

def get_index_list(url,data=None):
    web_data=requests.get(url)
    time.sleep(4)
    soup=BeautifulSoup(web_data.text,'lxml')

    titles=soup.select('#ATTR_ENTRY_ > div.attraction_clarity_cell > div > div > div.listing_info > div.listing_title > a[target="_blank"]')
    images=soup.select('img[width="180"]')
    cates=soup.select('#ATTR_ENTRY_ > div.attraction_clarity_cell > div > div > div.listing_info > div.tag_line > div')
    if data==None:
        for title,img,cate in zip(titles,images,cates):
            data={
                'title':title.get_text(),
                'url':'https://www.tripadvisor.cn'+title.get('href'),
                'img':img.get('src'),
                'cate':list(cate.stripped_strings)
            }
            print(data)

for url in urls:
    get_index_list(url)