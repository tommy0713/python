from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()

prefs = {"profile.managed_default_content_settings.images": 2,'permissions.default.stylesheet':2}
options.add_experimental_option("prefs", prefs)
# 不顯示頁面,在背景執行
# options.add_argument("--headless")
driver = webdriver.Chrome(executable_path=r"C:\Users\FX516PM\Desktop\chromedriver.exe",chrome_options=options)

driver.maximize_window()

url="https://histock.tw/stock/2201"
driver.get(url)
page=driver.page_source

soup = BeautifulSoup(page,"lxml")


stock = soup.select("table.tb-stock.tbPerform tr:nth-child(7) td:nth-child(2) span.clr-rd")

print(stock.text)


driver.quit()