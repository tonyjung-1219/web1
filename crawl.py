import time
import re
import requests
from datetime import date, timedelta, timezone, datetime
from bs4 import BeautifulSoup

start_cnt = 326

start_date = datetime.date(2021,3,7)
print(start_date)

week = timedelta(days=7)

current_date = start_date + week
print(current_date)

today = date.today()

print(today)



# def find_url():
#     start_date = datetime(2021, 3, 7, 12, 00, 00)
#     week = timedelta(days=7)
#     end_date = start_date + week
#     date_list += [start_date + timedelta(days=x) for x in range(7)]
#     print(date_list)
        

# find_url()

url = "http://www.jesuslovechurch.kr/EZ/rb/view.asp?BoardModule=Media&tbcode=media01&code=\
    &page=1&seq={num}&search_target=&search_keyword=".format(num=2)













# img_url = "http://www.jesuslovechurch.kr/upload_data/Media/media01/DefaultImage.jpg"

# browser.get(url)

# res = requests.get(url)
# soup = BeautifulSoup(res.text, "lxml")

# #스크롤 최하단으로 이동
# browser.execute_script("window.scrollTo(0,400)")

# # 주일 설교 버튼 클릭
# index = browser.find_element_by_xpath("//*[@id='work-carousel']/div[1]/div/div[6]/div/div[1]/div").click()

# # 스크롤 이동
# browser.execute_script("window.scrollTo(0,400)")
# soup_url = browser.current_url

# res = requests.get(soup_url)
# soup = BeautifulSoup(res.text, "lxml")

# # # 주일 설교 제목
# video_title = "\"제목 : " + soup.b.get_text() + '\"'
# print(video_title)

# # # 주일 설교 날짜
# video_date = soup.select('h6')[2]
# video_date_text = "\"" + video_date.get_text() + "\""
# print(video_date_text)

# # 본문 구절
# bible = soup.select('h6')[0]
# bible_text = "\"" + bible.get_text() + "\""

# print(bible_text)
# # 스크롤 다시 이동
# browser.execute_script("window.scrollTo(0,510)")

# # 주일 설교 동영상
# elem = browser.find_element_by_id("my-video_html5_api")
# video_play = "\"" + elem.get_attribute("src") + "\""
# print(video_play)

# browser.quit()