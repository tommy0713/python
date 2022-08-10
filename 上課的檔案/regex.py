import re
pattern1=r'c[\D]t'
pattern2='bird'
string='dog run to cat'

text='QvQ,Q123456789,1234567890,taichung'

qq=r'([A-Z]\d{9}),([A-Za-z]+$)'
ww=r'[A-Za-z]+$'
x=re.search(r'([A-Z]\d{9}),.+,([A-Za-z]+)','QvQ,Q123456789,1234567890,taichung')
print(x.group())
