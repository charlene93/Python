# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import urllib.request

start_url="http://www.mmjpg.com/"
def get_girls_urls(url):
    web_data=requests.get(url)
    #web_data.text将网页数据变成可读
    soup=BeautifulSoup(web_data.text,'lxml')
    html=soup.select('body > div.topbar > div.subnav > a')
    for list in html:
        print(list.get_text())
get_girls_urls(start_url)