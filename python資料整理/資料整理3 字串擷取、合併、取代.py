import numpy as np
import pandas as pd

#%%
data = pd.read_csv('C:/0413銷售資料.txt', encoding='utf-8',sep='\s+') 
#擷取 astype新增col並轉乘string形式
data['年月'] = data['營業日期'].astype(str).str[0:6]
#合併
data['日期+條碼'] = data['營業日期'].astype(str)+'-'+data['商品編號'].astype(str)
#取代
data['商品編號'].replace(7690393,'衛生紙',inplace =True)
