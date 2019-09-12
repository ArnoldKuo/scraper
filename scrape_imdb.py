from bs4 import BeautifulSoup
import requests

res = requests.get('http://www.imdb.com/chart/boxoffice')
soup = BeautifulSoup(res.text, "html5lib")

title=[]
for item in soup.select('.titleColumn'):
   title.append(item.get_text().lstrip().replace('\n','').ljust(50))

gross=[]
for item in soup.select('.secondaryInfo'):
   gross.append(item.get_text().ljust(10))

weeks=[]
for item in soup.select('.weeksColumn'):
   weeks.append(item.get_text())
   
#assign to a data structure
movie = {
	'Title': title,
	'Gross': gross,
	'Weeks': weeks
}

#print out the data structure
for i in range(0,len(title)):
    print(movie['Title'][i], movie['Gross'][i], movie['Weeks'][i])
