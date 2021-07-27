from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('hotfFRJhCHRyF24HahrG7jd/7tMAqsk6mDDul+1nI/rH2g4u47I9+EsiWBZ7NPMOiPP2g3eJbisQHfdwBnVE9ql1gxc67x/zNQLPTmpk9kIsnkB9EmaCf5G2RnULZ1HUCb4bDpOCAcmQnZKwYZfMJgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9687db7e5cc41ea498ae8af3e51af2e5')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

i []
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '我不了解你在說甚麼DX'

#你好的不同回答
    if msg == 'hi':
        r = 'Hello!你好啊?我的朋友'
    elif msg == 'Hi':
        r = 'Hello!你好啊?我的朋友'
    elif msg == 'hello':
        r = 'Hello!你好啊?我的朋友'
    elif msg == 'hello':
        r = 'Hello!你好啊?我的朋友'

    elif msg == 'hi?':
        r = 'Hello!你好啊?我的朋友'
    elif msg == 'Hi?':
        r = 'Hello!你好啊?我的朋友'
    elif msg == 'hello?':
        r = 'Hello!你好啊?我的朋友'
    elif msg == 'hello?':
        r = 'Hello!你好啊?我的朋友'

    elif msg == '你好':
        r = '你好啊?哈哈'
    elif msg == '你好嗎':
        r = '我很好, 你?'
    elif msg == '你好嗎?':
        r = '我很好, 你?'
    elif msg == '也好':
        r = '那就好'
    elif msg == '很好':
        r = '那就好'
    elif msg == '也很好':
        r = '那就好'

    elif msg == '不好':
        r = '怎麼了嗎?我的朋友'
    elif msg == '不太好':
        r = '怎麼了嗎?我的朋友'
    elif msg == '你好嗎?':
        r = '我很好, 你?'

    elif msg == '還好':
        r = '那就好我的朋友'
    elif msg == '很好':
        r = '那就好我的朋友'
    elif msg == '也很好':
        r = '那就好我的朋友'

    elif msg == '你好厲害':
        r = '謝謝'
    elif msg == '嘿':
        r = '??'
    elif msg == '嘿嘿':
        r = '嗯?'

    elif msg == '你幾歲?':
        r = '我14歲喔'
    elif msg == '你幾歲':
        r = '我14歲啦哈哈'



#回答你是誰
    elif msg == '你是誰':
        r = '我是虛擬語聖DX'
    elif msg == '你是誰?':
        r = '我是虛擬語聖DX'
    

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()