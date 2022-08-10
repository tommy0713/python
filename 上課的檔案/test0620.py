import requests
from bs4 import BeautifulSoup
import json
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
           AppleWebKit/537.36 (KHTML, like Gecko)\
           Chrome/102.0.0.0 Safari/537.36'}
url="https://www.taiwanstat.com/realtime/rain-ph/data/data.json"
r = requests.get(url,headers=header)
data = json.loads(r.text)
PH=[]

for i in data:
    PH.append({'地點':i['title'],'avg':i['this_avg']})

print(PH)