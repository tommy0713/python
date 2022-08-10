from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()

# #禁止圖片和css加載
prefs = {"profile.managed_default_content_settings.images": 2,'permissions.default.stylesheet':2}
options.add_experimental_option("prefs", prefs)
# 不顯示頁面,在背景執行
# options.add_argument("--headless")
driver = webdriver.Chrome(executable_path=r"C:\Users\FX516PM\Desktop\chromedriver.exe",chrome_options=options)
# driver = webdriver.Chrome(executable_path=r"C:\Users\FX516PM\Desktop\chromedriver.exe")
# 設定網頁大小及在螢幕的位置
# driver.set_window_position(0,0)
# driver.set_window_size(300,600)
driver.maximize_window()

url="https://www.momoshop.com.tw/search/searchShop.jsp?keyword=iphone&searchType=1&cateLevel=0&cateCode=&curPage=1&_isFuzzy=0&showType=chessboardType"
driver.get(url)
page=driver.page_source

soup = BeautifulSoup(page,"lxml")
name = soup.select("h3.prdName")
price = soup.select("span.price b")

for i in range(len(name)):
    print(name[i].text)
    print(price[i].text)