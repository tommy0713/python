import requests
from bs4 import BeautifulSoup
import json
url = "https://udn.com/search/word/2/新冠肺炎"
r = requests.get(url)
if r.status_code < 200 or r.status_code >= 300:
    print('連線失敗')
else:
    print('連線成功')
    page = r.text
    soup = BeautifulSoup(page, 'lxml')
    x=soup.select(".story-list__text h2 a")
    timeList = soup.select(".story-list__text time.story-list__time")
    title=[]
    url=[]
    times = []
    for i in range(len(x)):
        print(i+1,":",x[i].text)
        print(x[i].get("href"))
        title.append(x[i].text)
        url.append(x[i].get("href"))

    for i in timeList:
        times.append(i.text)
        print(i.text)
    newslist=[]
    # 將所有資料合併
    for index in range(len(title)):
        newslist.append({'title':title[index],'url':url[index],'times':times[index]})

