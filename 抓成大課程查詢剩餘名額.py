#-*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import re


dept = input(">>> 先輸入你要哪個科系:")
path = "http://140.116.165.74/qry/qry001.php?dept_no=" + dept
url = requests.get(path)

#記得BeautifulSoup第一格是要填 HTML原始碼 也就是url.content
soup = BeautifulSoup(url.content, 'html.parser')

#不能寫class = 'course_y0'
#re.compile(course) 可以是 course_y0 course_y1 y2....可以對應到不同年級
for each_class in soup.find_all('tr', {'class':re.compile('course')}):
	td = each_class.find_all('td')
	print(td[1].string , td[2].string , " ",td[10].string , end='')
	print("\t" ,  "目前有" , td[14].string , "人選課。" , end='')
	if td[15].string == "額滿": 
		print("\t" , "這堂課額滿了") 
	else: 
		print("\t" , "還有", td[15].string , "個名額")

		
		
		
		
'''
對應表
第 0 個string是 通識中心         GE 
第 1 個string是 A9 
第 2 個string是 010 
第 3 個string是 A942300 
第 4 個string是   
第 5 個string是   
第 6 個string是   
第 7 個string是 科際整合 
第 8 個string是   
第 9 個string是 N 
第 10 個string是 全球暖化與極端氣候事件 
第 11 個string是 必修 
第 12 個string是 2 
第 13 個string是 劉正千  
第 14 個string是 90 
第 15 個string是 額滿 
第 16 個string是 [1]7~8 
第 17 個string是 唯農大樓                      許文龍講堂 
第 18 個string是 None 
第 19 個string是 None 
第 20 個string是 否 
第 21 個string是 GE2521 
第 22 個string是 防災科技管理學分學程  
第 23 個string是 否
'''
'''
#不太能用each_class.td.next_sibling...顯示好像怪怪的
i=0
for each_sibling in :
	print("第",i,"個string是",each_sibling.string,"\n\n")
	i+=1'''


'''
#要點：不能直接print(a)的樣子，要用for迴圈
sum=0
for a in soup.find_all('a', target='_blank' ,href=re.compile("http://class-qry.acad.ncku.edu.tw")):
	print(a.string)
	sum+=1

print("總共找到", sum," 堂課！")
'''




