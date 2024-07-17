import json
import random
import re
import time
from urllib.parse import quote, urlsplit

import requests
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

def msearching(q):
    # crawl Code
    return mlist

# Wordk Space OAuth Tokens
app = App(token='')

## -- 식사메뉴 시작 -- ##
@app.message(re.compile("!메뉴"))
def regex(event, client, message, say):
    menu = ['피자', '탕수육', '짜장면', '짬뽕', '두부김치', '김치찜', '과자', '빵', '편의점', '라면', '김밥', '유뷰초밥', '스시', '회', '볶음짬뽕', '삼겹살', '김치찜', '김치찌개', '퇴근', '음료수', '고구마', '감자', '스테이크', '서브웨이', '햄버거', '맥도날드', '롯데리아', '맘스터치', '치킨', '닭발', '국수', '제육볶음', '파스타', '떡볶이', '쭈삼', ]
    result = random.choice(menu)
    say(result)

## -- 생존여부 확인 -- ##
@app.event("app_mention")  # 앱을 언급했을 때 @봇이름
def who_am_i(event, client, message, say):
    print('event:', event)
    print('client:', client)
    print('message:', message)
    say(f'hello! <@{event["user"]}>')

## --  # crawl code running -- ##
@app.message(re.compile("!순위"))
def regex(event, client, message, say):
  ###

## -- 앵무새 말 따라하기 시작 -- ##
follow = False
@app.message(re.compile("!ON"))
def talk():
    global follow
    follow = True

@app.message(re.compile("!OFF"))
def talk():
    global follow
    follow = False

@app.event("message")
def regex(event, client, message, say):
    global follow
    if follow == True:
        say(str(event['text']))
# ## -- 앵무새 말 따라하기 끝 -- ##

# Wordk Space APP-Level Tokens
if __name__ == '__main__':
    SocketModeHandler(app, '').start()
