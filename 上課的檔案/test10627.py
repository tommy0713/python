import re
string11=''' 陳小明 彰化縣中正路180巷12號2F 
            林小貓 台中市西區忠民南路23-6巷2弄100號
            林小狗 苗栗縣西區忠民南路23-6巷2弄100號'''
            
pattern11=r'(\w+)\s+(\w+[縣市])'
y=re.findall(pattern11,string11)

print(y)