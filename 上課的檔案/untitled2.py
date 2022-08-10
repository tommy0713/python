from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
options = Options()

prefs = {"profile.managed_default_content_settings.images": 2,'permissions.default.stylesheet':2}
options.add_experimental_option("prefs", prefs)
# 不顯示頁面,在背景執行
# options.add_argument("--headless")
s = Service(r"C:\Users\FX516PM\Desktop\chromedriver.exe")
driver = webdriver.Chrome(service=s,chrome_options=options)
driver.maximize_window()

url="https://goodinfo.tw/tw/StockDividendPolicy.asp?STOCK_ID=2330"
driver.get(url)
page=driver.page_source
soup = BeautifulSoup(page,"lxml")
stockid = soup.select("#tblDetail")
stock=pd.read_html(str(stockid))
stock=stock[0].values
stock1=[]
for i in range(30):
    stock1.append(list(stock[i]))
for i in range(34,len(stock)):
    stock1.append(list(stock[i]))
stock2=np.array(stock1)
stock3=pd.DataFrame(stock2)



driver.quit()