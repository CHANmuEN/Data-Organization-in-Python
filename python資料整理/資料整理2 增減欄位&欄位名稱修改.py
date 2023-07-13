import numpy as np
import pandas as pd

#%%
data = pd.read_csv('C:/0413銷售資料.txt', encoding='utf-8',sep='\s+') 
刪兩欄=data.drop(columns=['營業日期','購買時間'])
data['商品編號+1'] = data['商品編號']+1
#%%
data2=data.rename(columns={'營業日期':'日期','帳單編號':'發票'}) 
