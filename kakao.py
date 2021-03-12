# 설치한 Flask 패키지에서 Flask 모듈을 import 하여 사용
from flask import Flask, request, jsonify
from selenium import webdriver
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
import requests
import json

# options = webdriver.ChromeOptions()
# options.add_argument("headless")
# options.add_argument('window-size=1920x1080')

browser = webdriver.Chrome(
    "C:\\Python\\lowdb\\skill\\chromedriver_win32\\chromedriver.exe")

url = "http://www.jesuslovechurch.kr/html/main.asp"

img_url = "http://www.jesuslovechurch.kr/upload_data/Media/media01/DefaultImage.jpg"

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
video_title = "\"제목 : " + soup.b.get_text() + '\"'
print(video_title)

# # 주일 설교 날짜
video_date = soup.select('h6')[2]
video_date_text = "\"" + video_date.get_text() + "\""
print(video_date_text)

# 본문 구절
bible = soup.select('h6')[0]
bible_text = "\"" + bible.get_text() + "\""
print(bible_text)

# 스크롤 다시 이동
browser.execute_script("window.scrollTo(0,510)")

# 주일 설교 동영상
elem = browser.find_element_by_id("my-video_html5_api")
video_play = "\"" + elem.get_attribute("src") + "\""
print(video_play)

browser.quit()

app = Flask(__name__)


@app.route('/message', methods=['POST'])
def Message():

    dataSend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        "title": "video_title",
                        "description": "보물상자 안에는 뭐가 있을까",
                        "thumbnail": {
                            "imageUrl":         "https://lh3.googleusercontent.com/proxy/XNwgrM9QtISmvFZp7zW3QeEArM9mdTSM8GsI7CpAXzfUdXW_1t0WTiYXhjQc0y9gqQ6o0YjpRU120y2IkbFFYDZLn6J43qx_L1t65rezK45hPf0OOa47uKDtqt3BW-Pu"
                        },
                        "buttons": [
                            {
                                "action": "message",
                                          "label": "동영상 실행하기",
                                          "messageText": "video_play"
                            },
                            {
                                "action":  "message",
                                "label": "취소하기",
                                "messageText": "취소되었습니다"
                            }
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(dataSend)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
