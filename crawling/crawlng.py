from selenium import webdriver
import pprint
from bs4 import BeautifulSoup
from pprint import pprint
import requests
import time
import re


driver = webdriver.Chrome('/Users/munyeonglee/chromedriver')
time.sleep(3)

driver.get("http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun=")

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


#총 확진자 수
total = soup.find('dd',{'class': 'ca_value'}).text
print(total)

#오늘 확진자수
today = soup.find_all('p',{'class' : 'inner_value'})


total = today[0].text
print(total)
