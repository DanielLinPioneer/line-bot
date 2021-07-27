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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()