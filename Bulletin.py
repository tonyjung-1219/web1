from selenium import webdriver
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import sys
import requests
import json
from datetime import datetime
import time
import schedule

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[
    0]  # 크롬드라이버 버전 확인


options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument('window-size=1920x1080')

browser = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=options)


url = "http://www.jesuslovechurch.kr/html/main.asp"
browser.get(url)



#스크롤 최하단으로 이동
browser.execute_script("window.scrollTo(0,400)")

# 교회 소식 버튼 클릭
index = browser.find_element_by_xpath(
    "//*[@id='work-carousel']/div[1]/div/div[8]/div/div[2]/h3/a").click()

# 현재 url 확인
now_url = browser.current_url
this_url = requests.get(now_url)
soup = BeautifulSoup(this_url.text, "lxml")

# 스크롤 약간 이동
browser.execute_script("window.scrollTo(0,200)")

# 첫번째 문서 클릭

first_text = soup.find("h2", attrs={"class":"td_subject"}).get_text()

if first_text[0].isdigit() == True: # 해당 문서가 주보일 때 
    browser.find_element_by_xpath("/html/body/div[2]/div[3]/div/div/div[2]/div/div[2]/div/div/div[1]/div/div[2]/h2/a").click()
    browser.execute_script("window.scrollTo(0,650)") # 스크롤 상당히 이동

    bulletin_url = browser.current_url
    that_url = requests.get(bulletin_url)
    soup_b = BeautifulSoup(that_url.text, "lxml")

    Bulletin = browser.find_element_by_xpath("//*[@id='bo_v_con']/p[2]/img[1]")
    Bulletin_img = Bulletin.get_attribute("src")
    Bulletin_2 = browser.find_element_by_xpath("//*[@id='bo_v_con']/p[2]/img[2]")
    Bulletin_img_2 = Bulletin_2.get_attribute("src")
    print(Bulletin_img)
    print(Bulletin_img_2)
else:
    print("주보가 아닙니다.")

browser.quit()

# 오늘 날짜 확인
data_date = "C:\Python\lowdb\skill\data\\" + datetime.today().strftime('%Y-%m-%d') +".txt"
print(data_date)

# 데이터 작성
f = open(data_date, 'a')
data =  Bulletin_img + "\n" + Bulletin_img_2
f.write(data)
f.close()









