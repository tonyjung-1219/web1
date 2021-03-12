import time
import schedule
from flask import Flask, request, jsonify

app = Flask(__name__)

def sayhello():
    print("안녕하세요")

def printhello():
    print("Hello!")
 
 
schedule.every(2).seconds.do(printhello)
schedule.every(3).seconds.do(sayhello)




while True:
    schedule.run_pending()
    time.sleep(1)