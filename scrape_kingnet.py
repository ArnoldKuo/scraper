#!/usr/bin/env python
#-*-coding: utf-8 -*-

import sys
import requests
from selenium import webdriver
from bs4 import BeautifulSoup

#text = sys.argv[1]
#keyword = text.encode('utf-8')
#keyword = str(keyword).replace("'","").replace("b\\x","%").replace("\\x","%")

keyword = 'ACETAMINOPHEN'

url="https://www.kingnet.com.tw/knNew/medicine/medicine_search.html?keyword="+keyword
driver = webdriver.PhantomJS(executable_path=r'C:\Users\RKUO\phantomjs.exe')
driver.get(url)
soup = BeautifulSoup(driver.page_source, "html5lib")
driver.close()

items=soup.select('#medicineContentList')
anchors = items[0].find_all('a', {'target': '_blank', 'href': True})
for anchor in anchors:
    print(anchor.get_text(), anchor['href'])
