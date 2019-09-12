import requests
from bs4 import BeautifulSoup

url = 'http://www.azquotes.com/author/119-Alfred_Adler'
res = requests.post(url)
soup = BeautifulSoup(res.text,'html5lib')

items = soup.select('.title')

for i in range (1, 26):
    print(i)
    print(items[i].get_text())
