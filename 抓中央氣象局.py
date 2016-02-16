#-*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import re

url = requests.get("http://www.cwb.gov.tw/V7/forecast/f_index3.htm")
soup = BeautifulSoup(url.content, 'html.parser')

print("城市   溫度   降雨機率   天氣概況")
print("---------------------------------")
for each_city in soup.find_all('tr', id=re.compile('List')):
	td = each_city.find_all('td')
	print(td[0].string, td[1].string, td[2].string , end=' ')
	print("\t", td[3].a.div.img['title'])
	

