from bs4 import BeautifulSoup
import requests

url = 'http://www.appledaily.com.tw/realtimenews/section/new/'
res = requests.get(url)
soup = BeautifulSoup(res.text, "html5lib")

time=[]
for item in soup.select('.rtddt time'):
    time.append(item.text)

title=[]
for item in soup.select('.rtddt h1'):
    title.append(item.text)

category=[]
for item in soup.select('.rtddt h2'):
    category.append(item.text)

news = {
       'time': time,
       'title': title,
       'category':category
}

for i in range(0, len(time)):
    print(news['time'][i], news['title'][i], news['category'][i])
