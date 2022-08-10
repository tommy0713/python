from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# from selenium.webdriver.chrome.options import Options
# options = Options()

#禁止图片和css加载
# prefs = {"profile.managed_default_content_settings.images": 2,'permissions.default.stylesheet':2}
# options.add_experimental_option("prefs", prefs)

#不顯示視窗，背景抓資料
# options.add_argument("--headless")

s = Service(r"C:/Users/user/Desktop/chromedriver.exe")

# driver = webdriver.Chrome(service=s,chrome_options=option)
driver = webdriver.Chrome(service=s)


# driver.set_window_size(300, 600)
# driver.set_window_position(0, 0)
# driver.maximize_window()

# url="https://www.momoshop.com.tw/search/searchShop.jsp?keyword=iphone&searchType=1&cateLevel=0&cateCode=&curPage=1&_isFuzzy=0&showType=chessboardType"
# url="https://www.cwb.gov.tw/V8/C/W/week.html"
# url="https://histock.tw/stock/2201"
# url="https://goodinfo.tw/tw/StockDividendPolicy.asp?STOCK_ID=2330"
# url="https://histock.tw/login"
url="https://fea.mdu.edu.tw/zh_tw/CCETCOURSE?category%5B%5D=5d535a7ddf4feaa9160001ef&category%5B%5D=58d3a51c1d41c8605c000010&category%5B%5D=5ddf2485df4feaf1d20001ca&category%5B%5D=603602eadf4fea32fa0003cd&category%5B%5D=60360598df4feaf99d00014c"
#去首頁
driver.get(url)
#尋找 關鍵字:手作便當料理實務班 的超連結。並存入 data 元件
data=driver.find_element(By.PARTIAL_LINK_TEXT ,"手作便當料理實務班")
time.sleep(3)
#點擊找到的data 元件
data.click() 
time.sleep(3)
#回上一頁
driver.back()
time.sleep(3)
#尋找 關鍵字:Python 的超連結。並存入 data 元件
data=driver.find_element(By.PARTIAL_LINK_TEXT ,"Python")
#點擊找到的data 元件
data.click()