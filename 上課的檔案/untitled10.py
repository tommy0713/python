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
url="https://shopee.tw/buyer/login?next=https%3A%2F%2Fshopee.tw%2F"
driver.get(url)
driver.implicitly_wait(20)
while 1:
    try:
        driver.find_element(By.CSS_SELECTOR,'.pDzPRp').send_keys('0972361768')
        driver.find_element(By.CSS_SELECTOR,'.pDzPRp').send_keys('betty509')
        driver.find_element(By.CSS_SELECTOR,'button.wyhvVD._1EApiB.hq6WM5.L-VL8Q.cepDQ1._7w24N1').click()
        break
    except WebDriverException:
        time.sleep(3)