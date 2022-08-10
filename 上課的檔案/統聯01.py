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

s = Service(r"C:\Users\FX516PM\Desktop\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()

url="https://www.ubus.com.tw/"
driver.get(url)
driver.implicitly_wait(20)
driver.find_element(By.CSS_SELECTOR,'body > div.bg-light button:nth-child(3)').click()
driver.find_element(By.NAME,'MemberID').send_keys('L124993477')
driver.find_element(By.NAME,'password').send_keys('ymmot2024')
driver.find_element(By.CSS_SELECTOR,'#ubus_login').click()
# driver.execute_script('var q=document.documentElement.scrollTop=200000')
time.sleep(0.5)
# driver.execute_script("window.scrollTo(0, 100);")

start=Select(driver.find_element(By.CSS_SELECTOR,'#idx_beg'))
start.select_by_visible_text('台北轉運站')
end=Select(driver.find_element(By.CSS_SELECTOR,'#idx_end'))
end.select_by_visible_text('科技生活館站')
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR,"#idx_date").clear()
driver.find_element(By.CSS_SELECTOR,"#idx_date").send_keys('2022-07-01')
driver.find_element(By.CSS_SELECTOR,'#idx_time').click()
startTime=Select(driver.find_element(By.CSS_SELECTOR,'#idx_time'))
startTime.select_by_visible_text('09:00')
driver.find_element(By.CSS_SELECTOR,'#go_PT').click()
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR,'#pills-step2 > div > table > tbody > tr:nth-child(2) > td.py-4.px-3.h5.text-center.border-bottom > button').click()
driver.find_element(By.CSS_SELECTOR,'#AF').click()
driver.find_element(By.CSS_SELECTOR,'#booking_step3').click()
buy=[]
for i in range(1,29):
    data=driver.find_element(By.CSS_SELECTOR,'#car_mod > table > tbody > tr > th[data-value="{}"]'.format(i))
    if not "已售出" in data.text:
        buy.append(i)

order=[25,15,14,13,12,16,11,17]
for i in order:
    if i in buy:
        driver.find_element(By.CSS_SELECTOR,'#car_mod > table > tbody > tr > th[data-value="{}"]'.format(i)).click()
        break
driver.find_element(By.CSS_SELECTOR,'#booking_step4').click()
data=driver.find_element(By.CSS_SELECTOR,'#notice_i_agree')
if not data.is_selected():
    data.click()

# driver.find_element(By.CSS_SELECTOR,'#Booking_Complete button').click()