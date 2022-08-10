import requests
import re

url="https://www.cwb.gov.tw/Data/js/week/ChartData_Week_County_C.js?T=2022062022-5&_=1655736997224"
r=requests.get(url)
# print(r.text)

高溫pattern=r"C\':\{\'H\':\[(.+?)],\'L"
高溫=re.findall(高溫pattern, r.text)

低溫pattern=r"L\':\[(.+)]},\'F"
低溫=re.findall(低溫pattern, r.text)

高低溫pattern=r"C\':\{\'H\':\[(.+)].*\[(.+)]},\'F"
高低溫=re.findall(高低溫pattern, r.text)

低溫[0].split(',')                                                         