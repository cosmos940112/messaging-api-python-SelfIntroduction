from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def Birthday_guess():
    message = TemplateSendMessage(
        alt_text='生日',
        template=ButtonsTemplate(
            thumbnail_image_url="https://pic2.zhimg.com/v2-de4b8114e8408d5265503c8b41f59f85_b.jpg",
            title="我猜我猜我猜猜!!!",
            text="輸入生日後即獲得抽獎機會",
            actions=[
                DatetimePickerTemplateAction(
                    label="請選擇生日",
                    data="input_birthday",
                    mode='date',
                    initial='1990-01-01',
                    max='2019-03-10',
                    min='1930-01-01'
                ),
                URITemplateAction(
                    label="我反悔了...",
                    uri="https://youtu.be/072tU1tamd0"
                )
            ]
        )
    )
    return message

def Portfolio_Template():
    message = TemplateSendMessage(
        alt_text='Cosmos的相關連結如下：',
        template=CarouselTemplate(
             columns=[
                CarouselColumn(
                    text="Cosmos的相關連結如下：",
                    actions=[
                        URITemplateAction(
                            label="履歷",
                            uri='https://www.cakeresume.com/cosmos'
                        ),
                        URITemplateAction(
                            label="GitHub",
                            uri='https://github.com/cosmos940112'

                        ),
                        URITemplateAction(
                            label="GoogleDrive",
                            uri="https://drive.google.com/drive/u/2/folders/1C7RXhCrDaWpljqlnJOZl06re01ibDg09"
                        ),
                    ]
                )
            ]
        )
    )
    return message

def Tech_Template():
    message = TemplateSendMessage(
        alt_text='實作專案',
        template=CarouselTemplate(
             columns=[
                CarouselColumn(
                    title="虛擬射手(探討VR是否能提升專注力)",
                    actions=[
                        PostbackTemplateAction(
                            label="熟悉Unity應用操作，使用SteamVR 2.0套件",
                            data='1',
                        ),
                        PostbackTemplateAction(
                            label="熟悉VisualStudio，使用C#開發功能",
                            data='2'
                        ),
                        PostbackTemplateAction(
                            label="利用GitHub搜尋資源參考",
                            data="3"
                        ),
                        PostbackTemplateAction(
                            label="使用Blender場景、道具建模",
                            data="4"
                        ),
                        PostbackTemplateAction(
                            label="與使用者溝通後，提取建議並修改",
                            data="5"
                        ),
                        PostbackTemplateAction(
                            label="使用心率帶與腦波儀檢測並分析數據",
                            data="6"
                        )
                    ]
                ),
                CarouselColumn(
                    title="內勤人員報修系統",
                    actions=[
                        PostbackTemplateAction(
                            label="熟悉Eclipse，具環境建置與Git版本控管等相關經驗",
                            data='1',
                        ),
                        PostbackTemplateAction(
                            label="使用RatHat JBoss架設Local端的開發與測試環境",
                            data='2'
                        ),
                        PostbackTemplateAction(
                            label="使用JSF Web、PrimeFaces開發前端頁面",
                            data="3"
                        ),
                        PostbackTemplateAction(
                            label="使用Spring MVC架構，在Java Bean層處理前後端控制",
                            data="4"
                        ),
                        PostbackTemplateAction(
                            label="使用SQL語法控制MS SQL、NetBeans後端資料庫",
                            data="5"
                        )
                    ]
                ),
                CarouselColumn(
                    title="網購試衣新選擇(Line虛擬試衣間)",
                    actions=[
                        PostbackTemplateAction(
                            label="使用Messaging API、Heroku建置ChatBot環境",
                            data='1',
                        ),
                        PostbackTemplateAction(
                            label="使用LINE Official Account Manager功能串接",
                            data='2'
                        ),
                        PostbackTemplateAction(
                            label="使用Python OpenCV進行影像處理",
                            data="3"
                        ),
                        PostbackTemplateAction(
                            label="使用Python套件CMU openpose，將擷取到的特徵點，使用ROI套在相片的相應點",
                            data="4"
                        ),
                        PostbackTemplateAction(
                            label="使用LINE Bot Designer設計功能",
                            data="5"
                        )
                    ]
                )
            ]
        )
    )
    return message

def School_Template():
    message = TemplateSendMessage(
        alt_text='學校經歷',
        template=CarouselTemplate(
             columns=[
                CarouselColumn(
                    title="宜蘭大學",
                    text="資訊工程學系 2017 - 2021",
                    actions=[
                        MessageTemplateAction(
                            label="簡單介紹一下學習歷程",
                            text='學習歷程'
                        ),
                        MessageTemplateAction(
                            label="參加過什麼活動?",
                            text='參加活動'
                        ),
                        MessageTemplateAction(
                            label="參加過什麼比賽?",
                            text="比賽成果"
                        )
                    ]
                )
            ]
        )
    )
    return message

def Career_Template():
    message = TemplateSendMessage(
        alt_text='工作經歷',
        template=CarouselTemplate(
             columns=[
                CarouselColumn(
                    title="全球人壽保險股份有限公司",
                    text="系統設計師(實習生) 2020.7 - now",
                    actions=[
                        MessageTemplateAction(
                            label="簡單介紹一下實習經歷",
                            text='實習經歷'
                        ),
                        URITemplateAction(
                            label="看看我的實習心得",
                            uri="https://cosmosnoblog.blogspot.com/2020/09/blog-post.html"
                        )
                    ]
                )
            ]
        )
    )
    return message