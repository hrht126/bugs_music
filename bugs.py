# mongoDB연결
from pymongo import MongoClient
client = MongoClient('mongodb+srv://pmaker126:gkfngkxm126@cluster0.pemxrix.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

# 크롤링
import requests
from bs4 import BeautifulSoup

URL = "https://music.bugs.co.kr/chart"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(URL, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#CHARTrealtime > table > tbody > tr')

for tr in trs:
    rank = tr.select_one('.ranking > strong').text
                                        # ㄴstrong 랭킹만 나옴
    music = tr.select_one('.title').text
    artist = tr.select_one('.artist').text
    print(rank,music,artist)

# 딕셔너리로 mongoDB에 데이터 넣기
    doc = {
        'rank': rank,
        'music': music,
        'artist': artist
    }
    db.bugs.insert_one(doc)
    
