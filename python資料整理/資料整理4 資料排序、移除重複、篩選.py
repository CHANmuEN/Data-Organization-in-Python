import numpy as np
import pandas as pd
data = pd.read_csv('c:/0413銷售資料.txt',encoding='utf-8',sep='\s+')

#%% ascending遞減 

排序=data.sort_values(['商品編號'],ascending=False)
#subset 以哪個欄位作為基準 keep保留第一筆資料
移除重複=data.drop_duplicates(subset=['商品編號'],keep='first')
篩選=data.loc[data['商品編號'] == 7690393 ]

#%%