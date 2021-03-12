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
import schedule

def dawn_pray_crawl():
    chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]  # 크롬드라이버 버전 확인
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument('window-size=1920x1080')

    browser = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=options)

    url = "http://www.jesuslovechurch.kr/html/main.asp"

    browser.get(url)

    #스크롤 최하단으로 이동
    browser.execute_script("window.scrollTo(0,400)")

    # 새벽 설교 클릭
    browser.find_element_by_xpath("//*[@id='work-carousel']/div[1]/div/div[7]/div/div[2]/h3/a").click()

    # 스크롤 이동
    browser.execute_script("window.scrollTo(0,400)")
    dawn_pray_url = browser.current_url

    res_1 = requests.get(dawn_pray_url)
    soup_1 = BeautifulSoup(res_1.text, "lxml")

    # # 새벽 설교 제목
    video_title = soup_1.b.get_text()


    # # 새벽 설교 날짜
    video_date = soup_1.select('h6')[2]
    video_date_text = video_date.get_text()


    # 본문 구절 제목
    bible = soup_1.select('h6')[0]
    bible_text = bible.get_text()


    # 스크롤 다시 이동
    browser.execute_script("window.scrollTo(0,510)")

    # 새벽 설교 동영상
    elem = browser.find_element_by_id("my-video_html5_api")
    video_play = elem.get_attribute("src")


    browser.quit()

    
    if datetime.datetime.today().weekday() == 5 or 6:
        print("오늘은 새벽기도가 없는 날입니다")
        
    else:
        data_date = "C:\Python\lowdb\skill\data\\" + datetime.today().strftime('%Y-%m-%d') +".txt"
        print(data_date)

        # 데이터 작성
        f = open(data_date, 'w')
        data = video_title + "\n" + video_date_text + "\n" + bible_text + "\n" + video_play + "\n"
        f.write(data)
        f.close()


schedule.every().day.at("6:15").do(dawn_pray_crawl)

while True:
    schedule.run_pending()
    time.sleep(1)