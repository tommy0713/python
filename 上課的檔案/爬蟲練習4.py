import requests
import json
import time
import datetime
# file=open('news.txt','w+')
# file.write(r.text)
# file.close()
page = 0
index=0
key = '新冠肺炎'
date='2022-06-13'
dateA=time.strptime(date,'%Y-%m-%d')
end=0
# for i in range(page): 
while True:  
    if end == 1:
        break

    url="https://udn.com/api/more?page={}&id=search:{}&channelId=2&type=searchword&last_page=3994".\
        format(page+1,key)
    r=requests.get(url)
    page+=1
    data=json.loads(r.text)
    for i in range(len(data['lists'])):
        index+=1
        print(index,data["lists"][i]['title'][:10])
        print(data["lists"][i]['titleLink'])
        print(data["lists"][i]['time']['dateTime'][:10])
        newsDate=time.strptime(data["lists"][i]['time']['dateTime'][:10],'%Y-%m-%d')
        if newsDate < dateA:
            end=1
            break
        else:
            pass