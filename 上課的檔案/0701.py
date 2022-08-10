from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException
import numpy as np
from selenium.webdriver.support.ui import Select
options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
# 版本不一樣時加這行才不會閃退
s = Service(r"C:\Users\FX516PM\Desktop\chromedriver.exe")
driver = webdriver.Chrome(service=s,options=options)
driver.maximize_window()

url="https://isin.twse.com.tw/isin/class_i.jsp?kind=1"
driver.get(url)
driver.implicitly_wait(20)
stock1=Select(driver.find_element(By.CSS_SELECTOR,'body > form > table > tbody > tr:nth-child(4) > td:nth-child(2) > select'))
stock1.select_by_value('1')
stock1=Select(driver.find_element(By.CSS_SELECTOR,'body > form > table > tbody > tr:nth-child(5) > td:nth-child(2) > select'))
stock1.select_by_value('1')
driver.find_element(By.CSS_SELECTOR,'body > form > p:nth-child(4) > input[type=button]:nth-child(1)').click()
page=driver.page_source
soup = BeautifulSoup(page,"lxml")
stockid = soup.select("body > table.h4")
stock1=pd.read_html(str(stockid))
stock1=stock1[0].values
stock2=pd.DataFrame(stock1)
