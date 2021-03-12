import time
import schedule
 
#특정 함수 정의
def printhello():
    print("Hello!")
 
 
schedule.every(3).seconds.do(printhello) #30분마다 실행

 
#실제 실행하게 하는 코드
while True:
    schedule.run_pending()
    time.sleep(1)

