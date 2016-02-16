#-*- coding: UTF-8 -*-
import requests
import urllib.request
import re
import chardet

regex = '<title.*?>(.+?)</title>'
pattern = re.compile(regex)


while(1):
	path = input(">>> 請輸入網址: ")
	url = requests.get(path)
	
	
	charset=chardet.detect(url.content)
	#chardet自動偵測 url.content 的編碼
	
	
	title = re.findall(pattern, url.content.decode(charset['encoding'] , "replace")[0:2000])  
	#charset是一個dict結構，有兩個key: encoding, confidence，我們要的是encoding
	
	print(title)
	print("\n由 chardet.detect 取得的")
	print(charset['encoding'])
	
	print("\n由 url.encoding 取得的")
	print(url.encoding)

	print("\n由 headers.get_content_charset() 取得的")
	print(urllib.request.urlopen(path).headers.get_content_charset())
	print("\n")






