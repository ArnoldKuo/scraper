from bs4 import BeautifulSoup
import requests

host_url = 'http://www.saohua.com/shuku/ximurong'
res = requests.get(host_url)
soup = BeautifulSoup(res.text, "html5lib")

title_urls=[]

print("Scrap href from a webpage...")
for link in soup.findAll('a'):
    url=link.get('href')
    if (url!='http://www.saohua.com' and url!='http://www.saohua.com/shuku/'):
        url = host_url+'/'+url
        title_urls.append(url)
		
print("Fetching webpage content...")
contents=''
for url in title_urls:
    print(url)
    res = requests.get(url)
    res.encoding='gb2312'
    soup = BeautifulSoup(res.text, "html5lib")
    text = soup.text.split("HTMLBUILERPART0")
    contents+=text[0]
#    print(contents)

print("Writing to file...")
f=open("hsimuren.txt","w",encoding="utf-8")
f.write(contents)
f.close()
