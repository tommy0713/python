import requests
from bs4 import BeautifulSoup
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
           AppleWebKit/537.36 (KHTML, like Gecko)\
           Chrome/102.0.0.0 Safari/537.36'}
cookie={"over18":'1'}
url="https://www.ptt.cc/bbs/Gossiping/index.html"
r = requests.get(url,headers=header,cookies=cookie)
page=r.text
soup = BeautifulSoup(page, 'lxml')
x=soup.select(".title a")
y=soup.select(".meta .author")
title=[]

for i in range(len(x)):
    title.append({'title':x[i].text,'user':y[i].text})

print(title)
    