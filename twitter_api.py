#!/Users/hiro/.pyenv/shims/python3

import json, config #標準のjsonモジュールとconfig.pyの読み込み
from requests_oauthlib import OAuth1Session #OAuthのライブラリの読み込み

CK = config.api_key
CS = config.api_secret_key
AT = config.access_token
ATS = config.access_secret_token
twitter = OAuth1Session(CK, CS, AT, ATS) #認証処理

url = "https://api.twitter.com/1.1/statuses/user_timeline.json" #タイムライン取得エンドポイント

params ={'count' : 5} #取得数
res = twitter.get(url, params = params)

if res.status_code == 200: #正常通信出来た場合
    timelines = json.loads(res.text) #レスポンスからタイムラインリストを取得
    for line in timelines: #タイムラインリストをループ処理
        print(line['user']['name']+'::'+line['text'])
        print(line['created_at'])
        print('*******************************************')
else: #正常通信出来なかった場合
    print("Failed: %d" % res.status_code)
