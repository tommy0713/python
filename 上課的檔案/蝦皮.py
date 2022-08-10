from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import numpy as np
from selenium.common.exceptions import WebDriverException
s = Service(r"C:\Users\FX516PM\Desktop\chromedriver.exe")
# driver = webdriver.Chrome(service=s,chrome_options=option)
driver = webdriver.Chrome(service=s)
url="https://user.gamer.com.tw/login.php"
driver.get(url)
driver.implicitly_wait(20)
while 1:
    try:
        driver.find_element(By.NAME,'userid').send_keys('tommy40114')
        driver.find_element(By.NAME,'password').send_keys('ymmot2024')
        driver.find_element(By.CSS_SELECTOR,'#btn-login').click()
        break
    except WebDriverException:
        time.sleep(3)