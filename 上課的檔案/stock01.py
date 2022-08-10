from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
options = Options()

prefs = {"profile.managed_default_content_settings.images": 2,'permissions.default.stylesheet':2}
options.add_experimental_option("prefs", prefs)
# 不顯示頁面,在背景執行
# options.add_argument("--headless")
s = Service(r"C:\Users\FX516PM\Desktop\chromedriver.exe")
driver = webdriver.Chrome(service=s,chrome_options=options)
driver.maximize_window()

url="https://histock.tw/stock/2201"
driver.get(url)
page=driver.page_source

data=pd.read_html(page)[0].values

# soup = BeautifulSoup(page,"lxml")

# stockid = soup.select("#LBlock_3 table tr th ")
# stockid = stockid[3:]
# stock=[]

# for i in stockid:
#     stock.append({'週期':i.text})
#     print(i.text)
    
# percent=soup.select("#LBlock_3 table tr td span")  
# for i in percent:
#     print(i.text)
# for i in range(len(stockid)):
#     stock[i]['裕隆']=percent[2*i].text
#     stock[i]['大盤']=percent[2*i+1].text
    

driver.quit()