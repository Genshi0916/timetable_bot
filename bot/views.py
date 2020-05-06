import json
import requests
import datetime
from bot.serif import serif_monday
from bot.serif import serif_tuesday
from bot.serif import serif_wednesday
from bot.serif import serif_thursday
from bot.serif import serif_friday
from django.shortcuts import render
from django.http import HttpResponse

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'
ACCESS_TOKEN = 'k5hVF4eV4mqRMh70Fpu1sF5GGleGYJ5/NHqPwUcOtkb/VVaY+fPN6CBlOPIOL06e1Je0Ja4H1C8e8ScQWw820SHp9eox6t/pl40tGx9ZJwRK08lfEXULijIcJFzKPIwNlEsnSLgWkx3AJJkelOOWzAdB04t89/1O/w1cDnyilFU='
HEADER = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + ACCESS_TOKEN
}

def index(request):
    return HttpResponse("This is bot api.")



def reply_text(reply_token,text):
    @handler.add(MessageEvent, message=TextMessage)
    def handle_text_message(event):
        aaa = event.message.text
        reply = aaa
        # weekday = datetime.date.today().weekday()
        # if weekday==0:
        #     reply = serif_tuesday
        # elif weekday==1:
        #     reply = serif_wednesday
        # elif weekday==2:
        #     reply = serif_thursday
        # elif weekday==3:
        #     reply = serif_friday
        # elif weekday==6:
        #     reply = serif_monday
        # # elif aaa =="今日":
        # #     reply="今日の授業はまるまるです"
        # else: reply = "明日は授業ないよ"


        payload = {
            "replyToken":reply_token,
            "messages":[
                    {
                        "type":"text",
                        "text": reply
                    }
                ]
        }

        requests.post(REPLY_ENDPOINT,headers=HEADER,data=json.dumps(payload))
        return reply

def callback(request):
    reply = ""
    request_json = json.loads(request.body.decode('utf-8'))
    for i in request_json['events']:
        reply_token = i['replyToken']
        message_type = i['message']['type']
        if message_type == 'text':
            text = i['message']['text']
            reply +=reply_text(reply_token,text)

    return HttpResponse(reply)
