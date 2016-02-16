#-*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup




while(1):
	path = input(">>> 請輸入網址: ")
	url = requests.get(path)
	
	#記得BeautifulSoup第一格是要填 HTML原始碼 也就是url.content
	soup = BeautifulSoup(url.content, 'html.parser')
	
	charset=chardet.detect(url.content)
	
	print(soup.title.string)

	





