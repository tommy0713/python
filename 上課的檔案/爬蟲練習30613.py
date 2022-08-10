import requests
from bs4 import BeautifulSoup
import pymysql

db = pymysql.connect(host='127.0.0.1', user='QvQ',
                     passwd='19950713', database='news')

cursor = db.cursor()

url = "https://udn.com/search/word/2/新冠肺炎"
r = requests.get(url)
if r.status_code < 200 or r.status_code >= 300:
    print('連線失敗')
else:
    print('連線成功')
    page = r.text
    soup = BeautifulSoup(page, 'lxml')
    x = soup.select(".story-list__text h2 a")
    newslist = []
    for i in range(len(x)):
        newslist.append({'title': x[i].text, 'url': x[i].get("href")})
        
    times = soup.select(".story-list__text time.story-list__time")

    # 很多資料要合成的話一定是用range(len( ))
    for i in range(len(newslist)):
        newslist[i]['time'] = times[i].text[:10]

    for i in newslist:
        sql="select * from news where title='{}' and date='{}'".\
            format(i['title'],i['time'])
        cursor.execute(sql)
        db.commit()

        #獲得儲存的資料 
        data=cursor.fetchall()

        # 檢查資料庫中有沒有重複資料
        if len(data) > 0:
            pass
            print(i['title'],'重複,不儲存')
        else:
            sql = "insert into news (title,url,date) value ('{}','{}','{}')".\
                format(i['title'],i['url'], i['time'])
            cursor.execute(sql)
            # 儲存資料在cursor
    
    db.commit()
    # 將儲存的資料放進資料庫

db.close()
