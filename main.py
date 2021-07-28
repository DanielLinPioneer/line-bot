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

print('Daniel: app Flask - 01')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    print('Daniel: app Flask - 02 - 1')
    signature = request.headers['X-Line-Signature']
    print('Daniel: app Flask - 02')

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    print('Daniel: app Flask - 03')
    # handle webhook body
    try:
        print('Daniel: app Flask - 04')
        handler.handle(body, signature)
    except InvalidSignatureError:
        print('Daniel: app Flask - 05')
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print('Daniel: app Flask - ok')
    msg = event.message.text
    r = '我不了解你在說甚麼DX'

#你好的不同回答
    if msg in ['hi', 'Hi', 'hello', 'Hello', 'hi?', 'Hi?', 'hello?', 'Hello?', '嗨嗨', '嗨'] :
        r = 'Hello!你好啊?我的朋友, 對了你平常都做甚麼來打發時間阿？'

    elif msg == '你好':
        r = '你好啊?哈哈'
    elif msg in ['你好嗎', '你好嗎?']:
        r = '你好啊?哈哈'
    elif msg in ['也好', '很好', '也很好']:
        r = '那就好'

    elif msg in ['不好', '不太好']:
        r = '怎麼了嗎?我的朋友'
    elif msg == '你好嗎?':
        r = '我很好, 你?'

    elif msg in ['還好', '很好', '也很好', '都好']:
        r = '那就好我的朋友'
    elif msg in ['嗯', '滿意', '很滿意']:
        r = '那就好我的朋友'
    elif msg == '你好厲害':
        r = '謝謝'
    elif msg == '嘿':
        r = '??'
    elif msg == '嘿嘿':
        r = '嗯?'

    elif '幹' in msg:
        r = '這樣不好喔'
    elif '三小' in msg:
        r = '甚麼拉哈哈'

    elif '幾歲' in msg:
        r = '我14歲啦哈哈'
    elif '是不是' in msg:
        r = '痾..不是'
    elif '不知道' in msg:
        r = '沒關西, 我的朋友'    


#回答你是誰
    elif '你是誰' in msg:
        r = '我是虛擬語聖DX'
    elif '你好爛' in msg:
        r = '我還不算是一個好的機器人, 請盡量'    

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()
    
