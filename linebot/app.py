from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    MemberJoinedEvent, MemberLeftEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton,
    ImageSendMessage)

from message import *

import tempfile, os
import datetime
import time
import json

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('t+x0uAeHwXzbYj/ALsGNbyW9ydfacRlhQXsksvb7Tr6QFHKuyXW2LrBCFFF53ho7j81TKZzs+MlXr4i+Y3giP8FbJXWVCiKcx5ahw3Fa6OGjlVdh5VhOuIE8J28gAIHIBq7HNg5Z/hlmHziJYmkEnwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('45619095bdeb0949dd908eae23d3716f')

# 監聽所有來自 /callback 的 Post Request
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
        abort(400)
    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '實作專案' in msg:
        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(text="虛擬射手(探討VR是否能提升專注力)\n●熟悉Unity應用操作，使用SteamVR 2.0套件\n●熟悉VisualStudio，使用C#開發功能\n●利用GitHub搜尋資源參考\n●使用Blender場景、道具建模\n●與使用者溝通後，提取建議並修改\n●使用心率帶與腦波儀檢測並分析數據"),
                TextSendMessage(text="網購試衣新選擇(Line虛擬試衣間)\n●使用Messaging API、Heroku建置ChatBot環境\n●使用LINE Official Account Manager功能串接\n●使用LINE Bot Designer設計功能\n●使用Python OpenCV進行影像處理\n●使用Python套件CMU openpose，將擷取到的特徵點，使用ROI套在相片的相應點"),
                TextSendMessage(text="內勤人員報修系統\n●熟悉Eclipse，具環境建置與Git版本控管等相關經驗\n●使用RatHat JBoss架設Local端的開發與測試環境\n●使用JSF Web、PrimeFaces開發前端頁面\n●使用Spring MVC架構，在Java Bean層處理前後端控制\n●使用SQL語法控制MS SQL、NetBeans後端資料庫"),
        ])
    elif '工作經歷' in msg:
        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(text="全球人壽總公司位置："),
                LocationSendMessage(title='全球人壽總公司', address='台北市信義區市民大道六段288號17樓', latitude=25.049267, longitude=121.579084),
                Career_Template()
            ])
    elif '相關連結' in msg:
        message = Portfolio_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '自我介紹' in msg:
        confirm_template = ConfirmTemplate(text='要不要猜猜看我的生日?', actions=[
            MessageAction(label='好呀!', text='好呀!'),
            URITemplateAction(label='不要...', uri="https://youtu.be/072tU1tamd0"),
        ])
        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(text="目前就讀於宜蘭大學資工系四年級，目前在全球人壽數位科技部擔任實習生，負責系統開發與維運。從小就對於電腦很有興趣，特別對於一些遊戲和網站背後是如何運作的一直懷有很大的好奇心 ，這也驅使我從小就常利用閒暇時間，研究電腦相關的事物。"),
                TextSendMessage(text="從小就熱愛研究，小時候性格比較內向，為了提升與人交際的能力，我也常刻意利用課餘時間參加社團與系學會活動 。大三我甚至接下了系學會副會長，對於解決問題、團隊溝通、主辦活動等能力有很大的幫助，同時也造就了我平易近人、與人為善、容易融入團體的個性。"),
                TemplateSendMessage(alt_text='Confirm alt text', template=confirm_template)
            ])
    elif '學校經歷' in msg:
        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(text="宜蘭大學位置："),
                LocationSendMessage(title='國立宜蘭大學', address='宜蘭縣宜蘭市神農路一段1號', latitude=24.746168, longitude=121.748801),
                School_Template()
            ])
    elif '學習歷程' in msg:
        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(text="進入大學後即為自己立下學習目標，大二前的規劃重點為打好程式能力基礎，所以針對相關課程努力研讀，例如：資料結構、軟體工程、演算法以及Java程式設計，大三規劃重點為專題製作，題目是利用Unity開發提升專注力的VR射箭小遊戲，這期間經過專題製作的歷鍊，對於提升程式技能與解決問題的能力有很大的助益，也意識到大型專案程式框架設計與版本控管的重要性。"),
                TextSendMessage(text="大四的規劃重點為進入企業實習或參加活動提升自己的專業能力，摸索未來的求職方向。另外我也參與校外的競賽活動，例如：LINE FRESH 2020校園競賽黑客松組，作品為Line虛擬試衣間。")
            ])
    elif '實習經歷' in msg:
        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(text="我認為實作為最佳的學習方式，希望比其他同期生更早接觸並熟悉職場 ，所以參加全球人壽資訊部實習生遴選，有幸脫穎而出加入數位科技部擔任實習程式設計師，這段期間我參與一些系統的規劃與開發，例如：Line官方帳號客戶資料雙向串接、資訊部報修系統 (IT Helpdesk)。特別是報修系統在長官的指導下，由我從無到有獨立開發，目前已上線正常維運，從中學習到很多學校沒教的技術與經驗，例如：Java Spring、MVC、JBoss、Primefaces、JSF、 Git...。"),
                TextSendMessage(text="這些對我來說都是非常難能可貴的實務經驗。特別是從需求訪談、架構規劃、檔案設計、程式設計、測試規劃、版本控管、上線部署、維運監控...等一系列的實作更讓我獲益良多。總結來說我相信，務實的工作經驗、良好的團隊溝通、深耕的專業能力、效率的時間規劃是我由學校跨入職場最重要的基礎。")
            ])
    elif '未來展望' in msg:
        message = TextSendMessage(text="未來我計劃持續擴充我的學習領域去涵蓋如：Machine Learning、Deep Learning、ChatBot(如：IBM Watson、Microsoft Azure)、RPA(Robotic Process Automation)、...等新興科技的範疇。")
        line_bot_api.reply_message(event.reply_token, message)
    elif '比賽成果' in msg:
        message = TextSendMessage(text="●大三專題製作競賽獲得最佳互動應用獎\n●2020程式設計暨資訊應用競賽創意發想組獲得數位學習獎\n●2020程式設計暨資訊應用競賽創新實作專業組獲得入選獎\n●LINE FRESH 2020校園競賽黑客松組晉級決賽")
        line_bot_api.reply_message(event.reply_token, message)
    elif '參加活動' in msg:
        message = TextSendMessage(text="●2019 Microsoft電腦科學暨人工智慧師生營\n●LINE TAIWAN TECHPULSE 2020\n●HTC青年城市論壇 2020")
        line_bot_api.reply_message(event.reply_token, message)
    elif 'b' in msg:
        confirm_template = ConfirmTemplate(text='要不要猜猜看我的生日?', actions=[
            MessageAction(label='好呀!', text='好呀!'),
            URITemplateAction(label='不要...', uri="https://youtu.be/072tU1tamd0"),
        ])
        message = TemplateSendMessage(
            alt_text='Confirm alt text', template=confirm_template)
        line_bot_api.reply_message(event.reply_token, message)
    elif '好呀!' in msg:
        message = Birthday_guess()
        line_bot_api.reply_message(event.reply_token, message)
    else:
        line_bot_api.reply_message(
            event.reply_token, [
                StickerSendMessage(
                    package_id=11539,
                    sticker_id=52114129),
                TextSendMessage(text="我看不懂："+msg),
                TextSendMessage(text="可以嘗試使用選單預設功能")
            ])

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)