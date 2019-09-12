#!/usr/bin/env python
#-*-coding: utf-8 -*-
import sys
import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.youtube.com/watch?v=CTFtOOh47oo&list=PLx0sYbCqOb8TBPRdmBHs5Iftvv9TPboYG'

res = requests.get(url)
soup = BeautifulSoup(res.text, "html5lib")

item = soup.select('.yt-uix-scroller-scroll-unit')
#for i in range(1,len(item)):
for i in range(1,10):
   print(i)
   username = str(item[i]['data-video-username'])
   print(username)
   url = str(item[i]['data-thumbnail-url'])
   url = str(url).split('?')
   print(url[0])
   vtitle = str(item[i]['data-video-title'])
   print(vtitle.encode('utf-8'))
   vid = str(item[i]['data-video-id'])
   print(vid)
   print('---------------------------------------------')


