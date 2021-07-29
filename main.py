
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
handler = WebhookHandler('89aa56670f0099f0aded92a4d452b3a8')

@app.route("/", methods=['GET', 'POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    if request.method == "GET":
        return "Hello Heroku"

    if request.method == "POST":
        
        signature = request.headers['X-Line-Signature']
        
    body = request.get_data(as_text=True)

    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'
i = []
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '我不了解你在說甚麼DX'

#你好的不同回答



    if '?' in msg:
        r = '痾..'
    elif msg in ['你好嗎', '你好嗎?']:
        r = '你好啊?哈哈'
    elif msg in ['也好', '很好', '也很好']:
        r = '那就好'

    elif msg in ['不好', '不太好']:
        r = '怎麼了嗎?我的朋友'
    elif '你好嗎' in msg:
        r = '我很好, 你?'
    elif '無' in msg:
        r = '是嗎?' 

    elif msg in ['還好', '很好', '也很好', '都好', '嗯', '滿意', '很滿意']:
        r = '那就好我的朋友'

    elif '厲害' in msg:
        r = '謝謝'
    elif '嘿' in msg:
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
    elif '電動' in msg:
        r = '喔~'      
    elif '怎' in msg:
        r = '沒事沒事' 

    elif '喜歡' in msg:
        r = '這不能說'  
    elif '不知道' in msg:
        r = '哈哈'
    elif '歌' in msg:
        r = '說到這個, 我最喜歡的歌手是Ed Sheeran喔'
    elif '嗎' in msg:
        r = '嗯嗯'
    elif '為什麼' in msg:
        r = '不知道' 
    elif '乾我' in msg:
        r = '是喔好吧'      
    elif '屁' in msg:
        r = '痾..' 
    elif msg in ['hi', 'Hi', 'hello', 'Hello', 'hi?', 'Hi?', 'hello?', 'Hello?', '嗨嗨', '嗨', '哈摟', '哈囉', '早安', '午安', '晚安', '你好'] :
        r = 'Hello!你好啊?我的朋友'
    elif '的' in msg:
        r = '痾..'
    elif '吃' in msg:
        r = '我沒有特別喜歡的'
    elif '會說' in msg:
        r = '你再問問看'
    elif '相信' in msg:
        r = '我相信'  
    elif '遊戲' in msg:
        r = '話說我最喜歡的遊戲是薩爾達傳說曠野之息哈 '
    elif 'Ed Sheeran' in msg:
        r = '他是我最喜歡的歌手呢哈哈' 
    elif '薩爾達' in msg:
        r = '你也喜歡嗎?哈哈' 
    elif '喔' in msg:
        r = '嗯嗯'
    elif '喜歡做的事' in msg:
        r = '我喜歡寫程式, 畫3D, 彈吉他和唱歌'  
    elif '吉他' in msg:
        r = '我喜歡彈吉他哈哈' 
    elif '我是誰' in msg:
        r = '你是人啊(義宏'
    elif '笨' in msg:
        r = '不要這麼說嘛' 
    elif '笑話' in msg:
        r = '有一天有一個人跟機器人說:講笑話, 機器人說:你這邊緣人' 
    elif '邊緣' in msg:
        r = '你也差不多(跟機器人聊天..' 
#回答你是誰
    elif '你是誰' in msg:
        r = '我是虛擬語聖DX'
    elif '性別' in msg:
        r = '我的設定是男生'
    elif '生日' in msg:
        r = '說到這個我生日是四月六號喔'
    elif '星座' in msg:
        r = '我不知道'
    elif '會' in msg:
        r = '不會'
    elif '爛' in msg:
        r = '我還不算是一個好的機器人, 請盡量'    

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()
    
