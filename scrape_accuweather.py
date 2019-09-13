from bs4 import BeautifulSoup
import requests
from selenium import webdriver

url = 'https://www.accuweather.com/en/tw/taipei-city/315078/weather-forecast/315078'
#res = requests.get(url)
#soup = BeautifulSoup(res.text, "html5lib")

driver = webdriver.Chrome(executable_path=r'C:\Users\RKUO\chromedriver.exe') # for Windows
driver.get(url)
soup = BeautifulSoup(driver.page_source, "html5lib")
driver.close()

item = soup.select('.temp')
temp = item[0].text
print("Current Temp:",temp.replace('\t','').replace('\n',''))

item = soup.select('.real-feel')
real = item[0].text
print("Real-Feel:", real.replace('\t','').replace('\n',''))

item = soup.select('.cond')
cond = item[0].text
print("Condition:",cond.replace('\t','').replace('\n',''))
