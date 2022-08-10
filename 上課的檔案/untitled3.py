from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
from bs4 import BeautifulSoup
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
# driver.maximize_window()

# url="https://www.momoshop.com.tw/search/searchShop.jsp?keyword=iphone&searchType=1&cateLevel=0&cateCode=&curPage=1&_isFuzzy=0&showType=chessboardType"
# url="https://www.cwb.gov.tw/V8/C/W/week.html"
# url="https://histock.tw/stock/2201"
url="https://goodinfo.tw/tw/StockDividendPolicy.asp?STOCK_ID=2330"
driver.get(url)

   


driver.quit() 





 