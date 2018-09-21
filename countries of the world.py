def print_line():

    print("*" * 50)
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 17:57:47 2018

@author: USER
"""
import pandas as pd # 引用套件並縮寫為 pd  
df = pd.read_csv('countries of the world.csv')  
#print(df.keys())
#print(select_df)
select_df = pd.DataFrame(df)
print(df.keys())
print(df.shape)

print_line()

import seaborn as sns
sns.set(style='whitegrid', context='notebook')
cols = ['Population', 'Area (sq. mi.)', 'Literacy (%)','Phones (per 1000)','Birthrate','Deathrate','Region']
#select_df.fillna(value=0)
#select_df.dropna(axis=0,how='any') 去除datasets中，行(axis=0)的項目

sns_plot=sns.pairplot(select_df[cols].dropna(axis=0,how='any'), hue = 'Region',size=2);# kind="reg"使用回歸
sns_plot.savefig('output.png')