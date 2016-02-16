
#-*- coding: UTF-8 -*-
import requests
import urllib.request
import re

# 明天再做
regex = '<title>(.+?)</title>'
pattern = re.compile(regex)


#url = input(">>> 請輸入網址: ")
'''
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
>>> r.status_code
200
>>> r.headers['content-type']
'application/json; charset=utf8'
>>> r.encoding
'utf-8'
>>> r.text
u'{"type":"User"...'
>>> r.json()
{u'private_gists': 419, u'total_private_repos': 77, ...}
'''
while(1):
	path = input(">>> 請輸入網址: ")
	url = requests.get(path)
	
	if(url.encoding == "ISO-8859-1"):
		encoding = "cp950"
	else:
		encoding = url.encoding
		
	title = re.findall(pattern, url.content.decode(encoding , "replace")[0:2000])  
	print(title)
	print(url.encoding)
	print(urllib.request.urlopen(path).headers.get_content_charset())


	
	
	
'''
htmlfile = urllib.request.urlopen(url)
htmltext = htmlfile.read() 
print(htmlfile.headers.get_content_charset(failobj="cp950"))
print(htmlfile.info().get_content_charset(failobj="cp950"))
response = htmltext.decode('utf-8',"ignore")
'''

  
#print(response)	




