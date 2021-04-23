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
from datetime import datetime, date
import os
from flask import abort
import glob

app = Flask(__name__)


def find_txtlist(title):
    global filst
    filst = sorted(
        glob.glob(f'C:\chatbot\jesuslove_church\web1-church_chat_bot\data\{title}\*'))
    filst.reverse()

def is_number(value):
    try :
        float(value)
        return True
    except ValueError:
        return False


def bible_text_url(bible_text):
    bible_text = bible_text.split(" ")
    bible_text = bible_text[2]
    bible_text_list = list(bible_text)
    global url
    if bible_text_list.count("\n") == 1:
        bible_text = bible_text_list[1]
        if is_number(bible_text) == True:
            bible_text_list.insert(1, "%20")
            url_title = ''.join(bible_text_list)
            url = f"https://www.bskorea.or.kr/bible/korbibReadpage.php?version=GAE&txtReadInfo={url_title}&rdoReadType=2&cVersion=&fontSize=20px"
        
        elif is_number(bible_text) == False:

            bible_text_list.insert(2, "%20")
            url_title = ''.join(bible_text_list)
            url = f"https://www.bskorea.or.kr/bible/korbibReadpage.php?version=GAE&txtReadInfo={url_title}&rdoReadType=2&cVersion=&fontSize=20px"
    
    elif bible_text_list.count("\n") == 2:
        bible_text_list.remove("\n")
        print(bible_text_list)
        bible_text = bible_text_list[1]
        if is_number(bible_text) == True:
            bible_text_list.insert(1, "%20")
            url_title = ''.join(bible_text_list)
            url = f"https://www.bskorea.or.kr/bible/korbibReadpage.php?version=GAE&txtReadInfo={url_title}&rdoReadType=2&cVersion=&fontSize=20px"
        
        elif is_number(bible_text) == False:

            bible_text_list.insert(2, "%20")
            url_title = ''.join(bible_text_list)
            url = f"https://www.bskorea.or.kr/bible/korbibReadpage.php?version=GAE&txtReadInfo={url_title}&rdoReadType=2&cVersion=&fontSize=20px"


@app.route('/Bulletin', methods=['POST'])
def Bulletin():

    find_txtlist('Bulletin')

    today_data = filst[0]
    f = open(today_data, 'r')
    lines = f.readlines()

    Bulletin_img = lines[0]
    Bulletin_img_2 = lines[1]
    f.close()

    dataSend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleImage": {
                        "imageUrl": Bulletin_img_2,
                        "altText": "아직 주보가 준비되지 않았습니다"
                    }
                }
            ]
        }
    }
    return jsonify(dataSend)

# @ app.route('/church_news', methods=['POST'])
# def church_news():


@ app.route('/dawn', methods=['POST'])
def pray():
    find_txtlist('dawn_pray')
    recent_data = filst[0]

    f = open(recent_data, 'r')
    lines = f.readlines()

    video_title_1 = lines[0]
    video_date_1_text = lines[1]
    bible_text = lines[2]
    video_play_1 = lines[3]
    f.close()

    bible_text_url(bible_text)
    

    dataSend = {
        "version": "2.0",
        "template": {
            "outputs": [
                    {
                        "basicCard": {
                            "title": video_title_1,
                            "description": video_date_1_text + bible_text,
                            "thumbnail": {
                                "imageUrl": "https://gp.godpeople.com/wp-content/uploads/2017/08/GettyImages-675485922.jpg",
                                "fixedRatio": False


                            },
                            "buttons": [
                                {
                                    "action": "webLink",
                                    "label": "본문구절 읽기",
                                    "webLinkUrl": url
                                },
                                {
                                    "action": "webLink",
                                    "label": "동영상 실행하기",
                                    "webLinkUrl": video_play_1
                                }


                            ]
                        }
                    }
            ],
            "quickReplies": [
                {"label": "처음으로", "action": "message",
                 "messageText": "처음으로 이동"},
                {"label": "지난 새벽기도", "action": "message",
                    "messageText": '이전 새벽기도 동영상'},
                {"label": "검색하기", "action": "message",
                 "messageText": "새벽기도 검색하기"}

            ]
        }
    }
    return jsonify(dataSend)


@app.route('/blockid', methods=['POST'])
def blockid():
    blockid_data = request.json['userRequest']['block']['id']
    dataSend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": blockid_data
                    }
                }
            ]
        }
    }
    return jsonify(dataSend)

##### 블럭 ID #####
# 새벽 기도 검색 : 2v9upyyfg68qfuemp5zi89b9
# 주일 설교 말씀 : nxbql1b5e799k7th40gtc4o9
# 새벽기도 : 28557q5fjgpj380k2naf8q6h
# 교회소개 : 8pe5vle0g7vtmfrx8yvj0itw
# 주보 : jmj3qdbibkykp2u14084jnbi
# 환영인사! : yvpydn0m8piv7y6tpu3hvc6p


@ app.route('/dawn_pray_search', methods=['POST'])
def Search_pray():
    date_json = request.json['action']['detailParams']['date']['origin']
    date_text = date_json.replace("-", "")

    search_data = "C:\\chatbot\\jesuslove_church\\web1-church_chat_bot\\data\\dawn_pray\\" + \
        date_text + "_dawn_pray.txt"
    try:
        f = open(search_data, 'r')
        lines = f.readlines()

        video_title = lines[0]
        video_date_text = lines[1]
        bible_text = lines[2]
        video_play = lines[3]
        f.close()

        bible_text_url(bible_text)

        

        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                        {
                            "basicCard": {
                                "title": video_title,
                                "description": video_date_text + bible_text,
                                "thumbnail": {
                                    "imageUrl": "https://gp.godpeople.com/wp-content/uploads/2017/08/GettyImages-675485922.jpg",
                                    "fixedRatio": False

                                },
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "본문구절 보기",
                                        "webLinkUrl": url
                                    },
                                    {
                                        "action": "webLink",
                                        "label": "동영상 실행하기",
                                        "webLinkUrl": video_play
                                    }

                                ]
                            }
                        }
                ],
                "quickReplies": [
                    {"label": "처음으로", "action": "message",
                     "messageText": '처음으로 이동'},
                    {"label": "다시 검색하기", "action": "message",
                     "messageText": '새벽기도 다시 검색하기'}
                ]
            }
        }
    except FileNotFoundError:
        text = "해당 정보가 없습니다. 새벽기도는 토요일, 일요일 쉬며 2021년 1월 25일부터 데이터가 존재합니다."
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                        {
                            "simpleText": {
                                "text": text
                            }
                        }
                ],
                "quickReplies": [
                    {"label": "처음으로", "action": "message",
                     "messageText": '처음으로 이동'},
                    {"label": "다시 검색하기", "action": "message",
                     "messageText": '새벽기도 다시 검색하기'},
                    {"label": "예배시간 확인하기", "action": "message",
                     "messageText": "예배시간 확인하기"}
                ]

            }
        }
    return jsonify(dataSend)


@ app.route('/date_plus_dawn', methods=['POST'])
def date_pray():
    find_txtlist('dawn_pray')
    title = []
    date = []
    bible = []
    video_url = []
    bible_url = []
    for i in filst[1:4]:
        recent_data = i

        f = open(recent_data, 'r')
        lines = f.readlines()
        title.append(lines[0])
        date.append(lines[1])
        bible.append(lines[2])
        video_url.append(lines[3])

        f.close()
    
    for i in bible[0:3]:
        bible_text_url(i)
        bible_url.append(url)
        

    

    dataSend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "carousel": {
                        "type": "basicCard",
                        "items": [
                            {
                                "title": title[0],
                                "description": date[0] + bible[0],
                                "thumbnail": {
                                    "imageUrl": "https://gp.godpeople.com/wp-content/uploads/2017/08/GettyImages-675485922.jpg"
                                },
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "본문구절 읽기",
                                        "webLinkUrl": bible_url[0]
                                    },
                                    {
                                        "action": "webLink",
                                        "label": "동영상 실행하기",
                                        "webLinkUrl": video_url[0]
                                    }

                                ]
                            },
                            {
                                "title": title[1],
                                "description": date[1] + bible[1],
                                "thumbnail": {
                                    "imageUrl": "https://gp.godpeople.com/wp-content/uploads/2017/08/GettyImages-675485922.jpg"
                                },
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "본문구절 읽기",
                                        "webLinkUrl": bible_url[1]
                                    },
                                    {
                                        "action": "webLink",
                                        "label": "동영상 실행하기",
                                        "webLinkUrl": video_url[1]
                                    }
                                ]
                            },
                            {
                                "title": title[2],
                                "description": date[2] + bible[2],
                                "thumbnail": {
                                    "imageUrl": "https://gp.godpeople.com/wp-content/uploads/2017/08/GettyImages-675485922.jpg"
                                },
                                "buttons": [

                                    {
                                        "action": "webLink",
                                        "label": "본문구절 읽기",
                                        "webLinkUrl": bible_url[2]
                                    },
                                    {
                                        "action":  "webLink",
                                        "label": "동영상 실행하기",
                                        "webLinkUrl": video_url[2]
                                    }
                                ]
                            }
                        ]
                    }
                }
            ],
            "quickReplies": [
                {"label": "처음으로", "action": "message",
                 "messageText": "처음으로 이동"},
                {"label": "새벽기도 검색하기", "action": "message",
                 "messageText": "새벽기도 검색하기"}

            ]

        }
    }
    return jsonify(dataSend)


@ app.route('/sunday', methods=['POST'])
def Sunday():
    find_txtlist("sunday")
    today_data = filst[0]

    f = open(today_data, 'r')

    lines = f.readlines()

    video_title = lines[0]
    video_date_text = lines[1]
    bible_text = lines[2]
    video_play = lines[3]
    f.close()

    bible_text_url(bible_text)
    

    dataSend = {
        "version": "2.0",
        "template": {
            "outputs": [
                    {
                        "basicCard": {
                            "title": video_title,
                            "description": video_date_text + bible_text,
                            "thumbnail": {
                                "imageUrl": "https://gp.godpeople.com/wp-content/uploads/2021/03/bible_T-534x420.jpg",
                                "fixedRatio": False,


                            },
                            "buttons": [
                                {
                                    "action": "webLink",
                                    "label": "본문구절 읽기",
                                    "webLinkUrl": url
                                },
                                {
                                    "action": "webLink",
                                    "label": "동영상 실행하기",
                                    "webLinkUrl": video_play
                                }

                            ]
                        }
                    }
            ],
            "quickReplies": [
                {"label": "처음으로", "action": "message",
                 "messageText": "처음으로 이동"},
                {"label": "지난 주일 예배", "action": "message",
                 "messageText": "이전 주일예배 동영상"},
                {"label": "주일 예배 검색하기", "action": "message",
                 "messageText": "주일 예배 검색하기"}

            ]
        }
    }

    return jsonify(dataSend)


@ app.route('/sunday_search', methods=['POST'])
def Search_sunday():
    date_json = request.json['action']['detailParams']['date']['origin']
    date_text = date_json.replace("-", "")

    search_data = "C:\\chatbot\\jesuslove_church\\web1-church_chat_bot\\data\\sunday\\" + \
        date_text + "_sunday.txt"
    try:
        f = open(search_data, 'r')
        lines = f.readlines()

        video_title = lines[0]
        video_date_text = lines[1]
        bible_text = lines[2]
        video_play = lines[3]
        f.close()
        

    except FileNotFoundError:
        year = int(date_text[0:4])
        month = int(date_text[4:6])
        day = int(date_text[6:8])

        if date(year, month, day).weekday() == 0:
            date_data = str(int(date_text) - 1)
        elif date(year, month, day).weekday() == 1:
            date_data = str(int(date_text) - 2)
        elif date(year, month, day).weekday() == 2:
            date_data = str(int(date_text) - 3)
        elif date(year, month, day).weekday() == 3:
            date_data = str(int(date_text) - 4)
        elif date(year, month, day).weekday() == 4:
            date_data = str(int(date_text) - 5)
        elif date(year, month, day).weekday() == 5:
            date_data = str(int(date_text) - 6)

        

        real_data = "C:\\chatbot\\jesuslove_church\\web1-church_chat_bot\\data\\sunday\\" + \
            date_data + "_sunday.txt"

        f = open(real_data, 'r')
        lines = f.readlines()

        video_title = lines[0]
        video_date_text = lines[1]
        bible_text = lines[2]
        video_play = lines[3]
        f.close()

        
    
    bible_text_url(bible_text)

    dataSend = {
        "version": "2.0",
        "template": {
            "outputs": [
                    {
                        "basicCard": {
                            "title": video_title,
                            "description": video_date_text + bible_text,
                            "thumbnail": {
                                "imageUrl": "https://gp.godpeople.com/wp-content/uploads/2021/03/bible_T-534x420.jpg",
                                

                            },
                            "buttons": [
                                {
                                    "action": "webLink",
                                    "label": "본문구절 읽기",
                                    "webLinkUrl": url
                                },
                                {
                                    "action": "webLink",
                                    "label": "동영상 실행하기",
                                    "webLinkUrl": video_play
                                }
                            ]
                        }
                    }
            ],
            "quickReplies": [
                {"label": "처음으로", "action": "message",
                 "messageText": '처음으로 이동'},
                {"label": "주일 예배 다시 검색하기", "action": "message",
                 "messageText": '주일 예배 다시 검색하기'}
            ]
        }
    }
    return jsonify(dataSend)


@ app.route('/last_sunday', methods=['POST'])
def last_sunday():
    find_txtlist('sunday')
    title = []
    date = []
    bible = []
    video_url = []
    bible_url = []
    for i in filst[1:4]:
        recent_data = i

        f = open(recent_data, 'r')
        lines = f.readlines()
        title.append(lines[0])
        date.append(lines[1])
        bible.append(lines[2])
        video_url.append(lines[3])
        f.close()
    
    for i in bible[0:3]:
        bible_text_url(i)
        bible_url.append(url)
    

    dataSend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "carousel": {
                        "type": "basicCard",
                        "items": [
                            {
                                "title": title[0],
                                "description": date[0] + bible[0],
                                "thumbnail": {
                                    "imageUrl": "https://gp.godpeople.com/wp-content/uploads/2021/03/bible_T-534x420.jpg"
                                },
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "본문구절 읽기",
                                        "webLinkUrl": bible_url[0]
                                    },
                                    {
                                        "action": "webLink",
                                        "label": "동영상 실행하기",
                                        "webLinkUrl": video_url[0]
                                    }

                                ]
                            },
                            {
                                "title": title[1],
                                "description": date[1] + bible[1],
                                "thumbnail": {
                                    "imageUrl": "https://gp.godpeople.com/wp-content/uploads/2021/03/bible_T-534x420.jpg"
                                },
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "본문구절 읽기",
                                        "webLinkUrl": bible_url[1]
                                    },
                                    {
                                        "action": "webLink",
                                        "label": "동영상 실행하기",
                                        "webLinkUrl": video_url[1]
                                    }
                                ]
                            },
                            {
                                "title": title[2],
                                "description": date[2] + bible[2],
                                "thumbnail": {
                                    "imageUrl": "https://gp.godpeople.com/wp-content/uploads/2021/03/bible_T-534x420.jpg"
                                },
                                "buttons": [

                                    {
                                        "action": "webLink",
                                        "label": "본문구절 읽기",
                                        "webLinkUrl": bible_url[2]
                                    },
                                    {
                                        "action":  "webLink",
                                        "label": "동영상 실행하기",
                                        "webLinkUrl": video_url[2]
                                    }
                                ]
                            }
                        ]
                    }
                }
            ],
            "quickReplies": [
                {"label": "처음으로", "action": "message",
                 "messageText": "처음으로 이동"},
                {"label": "주일예배 검색하기", "action": "message",
                 "messageText": "주일예배 검색하기"}

            ]

        }
    }
    return jsonify(dataSend)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
