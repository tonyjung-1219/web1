from selenium import webdriver
import chromedriver_autoinstaller
from selenium import webdriver
import re
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import sys
import requests
import time
from datetime import datetime
import time
import schedule

options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument('window-size=1920x1080')

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

try:
    browser = webdriver.Chrome(f'C:\chatbot\jesuslove_church\web1-church_chat_bot\{chrome_ver}\chromedriver.exe')   
except:
    chromedriver_autoinstaller.install(True)
    browser = webdriver.Chrome(f'C:\chatbot\jesuslove_church\web1-church_chat_bot\{chrome_ver}\chromedriver.exe')

browser.implicitly_wait(10)

url = "http://www.jesuslovechurch.kr/html/main.asp"

browser.get(url)

res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")

#스크롤 최하단으로 이동
browser.execute_script("window.scrollTo(0,400)")

# 주일 설교 버튼 클릭
index = browser.find_element_by_xpath(
    "//*[@id='work-carousel']/div[1]/div/div[6]/div/div[1]/div").click()

# 스크롤 이동
browser.execute_script("window.scrollTo(0,400)")
soup_url = browser.current_url
res = requests.get(soup_url)
soup = BeautifulSoup(res.text, "lxml")

# # 주일 설교 제목
video_title = soup.b.get_text()

# # 주일 설교 날짜
video_date = soup.select('h6')[2]
video_date_text = video_date.get_text()

# 본문 구절
bible = soup.select('h6')[0]
bible_text = bible.get_text()

# 스크롤 다시 이동
browser.execute_script("window.scrollTo(0,510)")

# 주일 설교 동영상
elem = browser.find_element_by_id("my-video_html5_api")
video_play = elem.get_attribute("src")

browser.quit()

first_split = list(video_date_text)
first_split = first_split[7:]
first_split.pop(4)
first_split.pop(6)
datename = "".join(first_split)

# 오늘 날짜 확인
data_date = "C:\\chatbot\\jesuslove_church\\web1-church_chat_bot\\data\\sunday\\" + datename + "_" +\
    "sunday" + ".txt"

# 데이터 작성
f = open(data_date, 'w')
data = video_title + "\n" + video_date_text + "\n" + bible_text + "\n" + video_play
f.write(data)
f.close()

browser.quit()