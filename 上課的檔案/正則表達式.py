import re


string10='''
"ID: 021523, Date: Feb/12/2017"
"ID: 021524, Date: Feb/12/2018"
"ID: 021525, Date: Feb/12/2019"
'''
pattern10=r'ID: (?P<id>\d+), Date: (.+)'
x=re.search(pattern10,string10)
uid=x.group('id')
date=x.group(2)

print(uid)

y=re.findall(pattern10,string10)

# print(id)
