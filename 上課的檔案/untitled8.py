import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
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
driver.maximize_window()
driver.implicitly_wait(20) # seconds

url="https://udn.com/search/word/2/iphone"
driver.get(url)
time.sleep(5)
driver.execute_script('var q=document.documentElement.scrollTop=200000')
time.sleep(5)
driver.execute_script('var q=document.documentElement.scrollTop=200000')
time.sleep(5)
driver.execute_script('var q=document.documentElement.scrollTop=2400')