from selenium import webdriver
import chromedriver_autoinstaller
from flask import Flask, request, jsonify
from selenium import webdriver
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
import requests
import json
from datetime import datetime 

app = Flask(__name__)

# chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[
#     0]  # 크롬드라이버 버전 확인


# options = webdriver.ChromeOptions()
# options.add_argument("headless")
# options.add_argument('window-size=1920x1080')

# browser = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=options)


# url = "http://www.jesuslovechurch.kr/html/main.asp"

# img_url = "https://gp.godpeople.com/wp-content/uploads/2021/03/bible_T-534x420.jpg"
# browser.get(url)

# res = requests.get(url)
# soup = BeautifulSoup(res.text, "lxml")

# #스크롤 최하단으로 이동
# browser.execute_script("window.scrollTo(0,400)")

# # 주일 설교 버튼 클릭
# index = browser.find_element_by_xpath(
#     "//*[@id='work-carousel']/div[1]/div/div[6]/div/div[1]/div").click()

# # 스크롤 이동
# browser.execute_script("window.scrollTo(0,400)")
# soup_url = browser.current_url
# res = requests.get(soup_url)
# soup = BeautifulSoup(res.text, "lxml")

# # # 주일 설교 제목
# video_title = soup.b.get_text()


# # # 주일 설교 날짜
# video_date = soup.select('h6')[2]
# video_date_text = video_date.get_text()


# # 본문 구절
# bible = soup.select('h6')[0]
# bible_text = bible.get_text()

# # 스크롤 다시 이동
# browser.execute_script("window.scrollTo(0,510)")

# # 주일 설교 동영상
# elem = browser.find_element_by_id("my-video_html5_api")
# video_play = elem.get_attribute("src")

# browser.back()

# dawn_img_url = "https://gp.godpeople.com/wp-content/uploads/2017/08/GettyImages-675485922.jpg"

# #스크롤 최하단으로 이동
# browser.execute_script("window.scrollTo(0,400)")

# # 새벽 설교 클릭
# browser.find_element_by_xpath(
#     "//*[@id='work-carousel']/div[1]/div/div[7]/div/div[2]/h3/a").click()

# # 스크롤 이동
# browser.execute_script("window.scrollTo(0,400)")
# dawn_pray_url = browser.current_url
# res_1 = requests.get(dawn_pray_url)
# soup_1 = BeautifulSoup(res_1.text, "lxml")

# # # 주일 설교 제목
# video_title_1 = soup_1.b.get_text()

# # # 주일 설교 날짜
# video_date_1 = soup_1.select('h6')[2]
# video_date_1_text = video_date_1.get_text()

# # 본문 구절 제목
# bible_1 = soup_1.select('h6')[0]
# bible_1_text = bible_1.get_text()

# # 스크롤 다시 이동
# browser.execute_script("window.scrollTo(0,510)")

# # 주일 설교 동영상
# elem_1 = browser.find_element_by_id("my-video_html5_api")
# video_play_1 = elem_1.get_attribute("src")

# url = "http://www.jesuslovechurch.kr/html/main.asp"
# browser.get(url)


# #스크롤 최하단으로 이동
# browser.execute_script("window.scrollTo(0,400)")

# # 교회 소식 버튼 클릭
# index = browser.find_element_by_xpath(
#     "//*[@id='work-carousel']/div[1]/div/div[8]/div/div[2]/h3/a").click()

# # 현재 url 확인
# now_url = browser.current_url
# this_url = requests.get(now_url)
# soup = BeautifulSoup(this_url.text, "lxml")

# # 스크롤 약간 이동
# browser.execute_script("window.scrollTo(0,200)")

# # 첫번째 문서 클릭

# first_text = soup.find("h2", attrs={"class": "td_subject"}).get_text()

# if first_text[0].isdigit() == True:  # 해당 문서가 주보일 때
#     browser.find_element_by_xpath(
#         "/html/body/div[2]/div[3]/div/div/div[2]/div/div[2]/div/div/div[1]/div/div[2]/h2/a").click()
#     browser.execute_script("window.scrollTo(0,650)")  # 스크롤 상당히 이동

#     bulletin_url = browser.current_url
#     that_url = requests.get(bulletin_url)
#     soup_b = BeautifulSoup(that_url.text, "lxml")

#     Bulletin = browser.find_element_by_xpath("//*[@id='bo_v_con']/p[2]/img[1]")
#     Bulletin_img = Bulletin.get_attribute("src")
#     Bulletin_2 = browser.find_element_by_xpath(
#         "//*[@id='bo_v_con']/p[2]/img[2]")
#     Bulletin_img_2 = Bulletin_2.get_attribute("src")
#     print(Bulletin_img)
#     print(Bulletin_img_2)
# else:
#     print("주보가 아닙니다.")

# browser.quit()



@app.route('/Bulletin', methods=['POST'])
def Bulletin():
    
    today_data = "C:\Python\lowdb\skill\data\\" + datetime.today().strftime('%Y-%m-%d') + ".txt"

    f = open(today_data, 'r')
    lines = f.readlines()
        
    Bulletin_img = lines[8]
    Bulletin_img_2 = lines[9]
    print(Bulletin_img)
    print(Bulletin_img_2)
    f.close()

    dataSend = {
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "simpleImage": {
                    "imageUrl": Bulletin_img,
                    "altText" : "아직 주보가 준비되지 않았습니다"
                }
            }
        ]
    }
}
    return jsonify(dataSend)


@ app.route('/dawn', methods=['POST'])
def pray():
        # global video_title_1
        # global video_date_1_text
        # global bible_1_text
        # global video_play_1

        today_data = "C:\Python\lowdb\skill\data\\" + datetime.today().strftime('%Y-%m-%d') + ".txt"

        f = open(today_data, 'r')
        lines = f.readlines()
        
        video_title_1 = lines[0]
        video_date_1_text = lines[1]
        bible_1_text  = lines[2]
        video_play_1 = lines[3]
        f.close()

        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "basicCard": {
                            "title": video_title_1,
                            "description": video_date_1_text + "\n" + bible_1_text,
                            "thumbnail": {
                                "imageUrl": "https://gp.godpeople.com/wp-content/uploads/2017/08/GettyImages-675485922.jpg",
                                "fixedRatio": False,


                            },
                            "buttons": [
                                {
                                    "action": "webLink",
                                    "label": "동영상 실행하기",
                                    "webLinkUrl": video_play_1
                                }


                            ]
                        }
                    }
                ]
            }
        }
        return jsonify(dataSend)

@ app.route('/message', methods=['POST'])
def Message():

        # global video_title
        # global video_date_text
        # global bible_text
        # global video_play
        # global soup_url

        today_data = "C:\Python\lowdb\skill\data\\" + datetime.today().strftime('%Y-%m-%d') + ".txt"

        f = open(today_data, 'r')
        lines = f.readlines()
        
        video_title = lines[4]
        video_date_text = lines[5]
        bible_text = lines[6]
        video_play = lines[7]
        f.close()
    
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "basicCard": {
                            "title": video_title,
                            "description": video_date_text + "\n" + bible_text,
                            "thumbnail": {
                                "imageUrl": "https://gp.godpeople.com/wp-content/uploads/2021/03/bible_T-534x420.jpg",
                                "fixedRatio": False,


                            },
                            "buttons": [
                                {
                                    "action": "webLink",
                                    "label": "동영상 실행하기",
                                    "webLinkUrl": video_play
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
