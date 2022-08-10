from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException
import numpy as np
# from selenium.webdriver.chrome.options import Options
# options = Options()

#禁止图片和css加载
# prefs = {"profile.managed_default_content_settings.images": 2,'permissions.default.stylesheet':2}
# options.add_experimental_option("prefs", prefs)

#不顯示視窗，背景抓資料
# options.add_argument("--headless")

s = Service(r"C:\Users\FX516PM\Desktop\chromedriver.exe")

# driver = webdriver.Chrome(service=s,chrome_options=option)
driver = webdriver.Chrome(service=s)


# driver.set_window_size(300, 600)
# driver.set_window_position(0, 0)
driver.maximize_window()

# url="https://www.momoshop.com.tw/search/searchShop.jsp?keyword=iphone&searchType=1&cateLevel=0&cateCode=&curPage=1&_isFuzzy=0&showType=chessboardType"
# url="https://www.cwb.gov.tw/V8/C/W/week.html"
# url="https://histock.tw/stock/2201"
# url="https://goodinfo.tw/tw/StockDividendPolicy.asp?STOCK_ID=2330"
# url="https://user.gamer.com.tw/login.php"
url="https://histock.tw/login"
driver.get(url)
driver.implicitly_wait(20)

while True:
    try:
        driver.find_element(By.NAME,"email").send_keys('tommy40114@gmail.com')
        driver.find_element(By.NAME,"password").send_keys('19950713')
        driver.find_element(By.CSS_SELECTOR,'input[type="submit"]').click()
        break
    except WebDriverException:
        print('error')
        time.sleep(5)
time.sleep(3)
# soup=BeautifulSoup(driver.page_source,'lxml')
# stockId=soup.select('table.tb-stock.tbTable.tbFutures')
# stock=pd.read_html(str(stockId))
stocks=['1101','1102','2027','2330','0050','00878']
page=[]
for i in stocks:
    url='https://histock.tw/stock/{}'.format(i)
    index=1
    while 1:
        try:
            driver.get(url)
            break
        except WebDriverException:
            print('error')
            time.sleep(index*3)
            index+=1
    print('success: '+url)
    page.append(driver.page_source)
pages=[]
pages2=[]
for i in range(len(page)):
    soup=BeautifulSoup(page[i],'lxml')
    stockId=soup.select('#RBlock_4 table.tb-stock.tbTable.tbFutures')
    stock=pd.read_html(str(stockId))
    stock=stock[0].values
    pages.append(np.array(stock))
    stock1=pd.DataFrame(stock)
    pages2.append(stock1)

driver.quit()



   

