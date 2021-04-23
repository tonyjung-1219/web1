from selenium import webdriver
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import requests
import json
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



# first_text = soup.find_all("h2", attrs={"class":"td_subject"})
first_text = []
for i in range(1,21):
    first_text.append(soup.select(".td_subject")[i].get_text())

second_text = first_text.copy()


for i in first_text:
    title_text = i[0]
    

    if title_text.isdigit() == True:
        first_text.remove(i)
    else:
        pass


for i in first_text:
    title_text = i[0]

    if title_text.isdigit() == True:
        first_text.remove(i)
    
    else:
        pass

news_title = first_text.copy()
news_main_text = []
news_img = []
news_url = []


for i in news_title:
    browser.execute_script("window.scrollTo(0,200)")
    index = second_text.index(i) + 1
    
    news_main_text.append(browser.find_element_by_xpath(f"/html/body/div[2]/div[3]/div/div/div[2]/div/div[2]/div/div/div[{index}]/div/div[2]/p").text)
    time.sleep(1)
    browser.find_element_by_xpath(f"/html/body/div[2]/div[3]/div/div/div[2]/div/div[2]/div/div/div[{index}]/div/div[2]/h2/a").click()
    news_url.append(browser.current_url)

    browser.execute_script("window.scrollTo(0,250)")

    time.sleep(1)
    img_tag = browser.find_elements_by_tag_name("img")[1]
    src = img_tag.get_attribute('src')
    news_img.append(src)

    time.sleep(1)

    browser.back()
    
browser.quit()
count = len(news_url)

# 오늘 날짜 확인
data_date = "C:\\chatbot\\jesuslove_church\\web1-church_chat_bot\\data\\news_memo.txt"

f = open(data_date, 'w')
# 데이터 작성
for i in range(0, count):
    data = news_title[i] + "\n" + news_main_text[i] + "\n" + news_img[i] + "\n" + news_url[i] + "\n"
    f.write(data)

f.close()



