import requests
from bs4 import BeautifulSoup
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
           AppleWebKit/537.36 (KHTML, like Gecko)\
           Chrome/102.0.0.0 Safari/537.36'}

payload={'tfield':'qqq','area':'www',
'select':'English','rad':'1','submit':'Submit'}
url="https://dobrev.com/cgi-bin/Post-Demo.pro"
r = requests.post(url,headers=header,data=payload)
soup = BeautifulSoup(r.text, 'lxml')

    
