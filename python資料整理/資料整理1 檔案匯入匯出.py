import numpy as np
import pandas as pd

#%%
'ASCII英文 gb18030中文 預設utf-8'
data = pd.read_csv('C:/0413銷售資料.txt', encoding='utf-8',sep='\s+') 
#%%
data.to_csv('D:/123.csv', encoding='utf_8_sig',index=0)
#%%