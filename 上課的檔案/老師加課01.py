#**************************************************************
import pandas as pd
# x=[0.25, 0.5, 0.75, 1.0] #python原生陣列型態
import numpy as np 
# y=np.array([0.25, 0.5, 0.75, 1.0]) #numpy陣列型態

#**************************************************************
#也可以透過python字典型態來做轉換

# #pandas可以完全相容python與numpy資料型態，無需特別去轉換
# a = pd.Series(x) #將python陣列轉換成pandas
# b = pd.Series(y) #將numpy陣列轉換成pandas

# a.index=['北區','中區','南區','東區'] #row(列) attribute
# #a.columns column(欄)attribute，一維無法使用，需多維
#**************************************************************
# #由多個 pandas series陣列 建立 pandas表格 (dataframe)
# x=pd.Series([1,2,3])
# x.index=['北區','中區','南區']
# y=pd.Series([4,5,6])
# y.index=['北區','中區','南區']

# #**************************************************************
# # #指定欄位名稱'第一欄'、'第二欄'
# z = pd.DataFrame({'A欄':[1,2,3],'B欄':[2,3,4]})
# z.index=['北區','中區','南區']
# # #重新指定欄位名稱'平板銷售額'、'手機銷售額'
# z.columns=['平板銷售額','手機銷售額']

#**************************************************************
#多維陣列pandas建立方法
#**************************************************************
#由python字典建立 pandas表格 (dataframe)
population_dict = {'California': 38332521,'Texas': 26448193,
    'New York': 19651127,'Florida': 19552860,'Illinois': 12882135}
# population = pd.Series(population_dict)

area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
'Florida': 170312, 'Illinois': 149995}
# area = pd.Series(area_dict)

states = pd.DataFrame({'population': population_dict,'area': area_dict})
x=states.values  #將pandas (states) 還原成numpy陣列
y=pd.DataFrame([[1,2,3],[4,5,6]])
y.index=['A','B']
y.columns=['大','中','小']

# #numpy二維陣列可以轉換成pandas dataframe

y=np.zeros([3,3])
z2=pd.DataFrame(y)
z2.columns=['平板銷售額','手機銷售額','3c銷售額']
z2.index=['北區','中區','南區']
ave=[23,25,18]
# z2['平均']=0
z2.insert(3,column="平均銷售",value=ave)
# z2=z2.append({},ignore_index=True)
z2=z2.append({'平板銷售額':1,'手機銷售額':2},ignore_index=True)
z2.index=['北區','中區','東區','合計']
# ***************************************************************
#刪除 dataframe 整欄
# z2=z2.drop(labels=['3c銷售額'],axis=1)
# x=z2.columns[2]
z2=z2.drop(columns=[z2.columns[2]])
z2=z2.drop(index=[z2.index[0]])
#刪除 dataframe 整列
# z2=z2.drop(labels=['東區'],axis=0)
# z2=z2.drop(index=['東區'])