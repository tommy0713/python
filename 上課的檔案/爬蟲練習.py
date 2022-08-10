import requests
from bs4 import BeautifulSoup
url = "https://udn.com/search/word/2/新冠肺炎"
r = requests.get(url)
if r.status_code < 200 or r.status_code >= 300:
    print('連線失敗')
else:
    print('連線成功')
    page = r.text
    soup = BeautifulSoup(page, 'lxml')
    x=soup.select(".story-list__text h2 a")

    # 空陣列儲存title和url
    title=[]
    url=[]
    
    # 3個for迴圈結果都一樣
    # index=1
    # for i in x:
    #     print(index,':',i.text)
    #     index+=1

    for i in range(len(x)):
        print(i+1,":",x[i].text)
        print(x[i].get("href"))
        title.append(x[i].text)
        url.append(x[i].get("href"))

    # for index,i in enumerate(x):
    #     print(index+1,":",x.text)
