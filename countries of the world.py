def print_line():

    print("*" * 50)
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 17:57:47 2018

@author: USER
"""
import pandas as pd # 引用套件並縮寫為 pd  
import matplotlib.pyplot as plt
df = pd.read_csv('countries of the world.csv')  
select_df = pd.DataFrame(df.dropna(axis=0,how='any'))
print(select_df.keys())
print(select_df.shape)
print_line()

print("GDP 集中量數:")
print("眾數", df["GDP ($ per capita)"].mode())
print("中位數",df["GDP ($ per capita)"].median())
print("四分位數",df["GDP ($ per capita)"].quantile(q=0.25),end='  ')
print(df["GDP ($ per capita)"].quantile(q=0.5),end='  ')
print(df["GDP ($ per capita)"].quantile(q=0.75))
print("平均數:",df["GDP ($ per capita)"].mean())
print("GDP 離散量數:")
print("全距",df["GDP ($ per capita)"].max()-df["GDP ($ per capita)"].min())
print("四分位差",df["GDP ($ per capita)"].quantile(0.25)-df["GDP ($ per capita)"].quantile(0.75))
print("變異數",df["GDP ($ per capita)"].var())
print("標準差",df["GDP ($ per capita)"].std())
#描述性統計
print(select_df["GDP ($ per capita)"].describe())

#畫散佈圖(GDP和Phones) 分別採用 seaborn和 .plot來做圖
import seaborn as sns
sns.set(style='whitegrid', context='notebook')
col = ["GDP ($ per capita)","Phones (per 1000)"]
sns_plot=sns.pairplot(select_df[col],size=2)
select_df[col].plot(kind="scatter", x="GDP ($ per capita)", y="Phones (per 1000)",title="Relationship between GDP and Phones")
print_line()
#多欄位間的散佈圖
#cols = ['Population', 'Area (sq. mi.)', 'Literacy (%)','Phones (per 1000)','Birthrate','Deathrate','Region']
#select_df.fillna(value=0)
#select_df.dropna(axis=0,how='any') 去除datasets中，行(axis=0)的項目
#sns_plot=sns.pairplot(select_df[cols].dropna(axis=0,how='any'), hue = 'Region',size=2);# kind="reg"使用回歸
#sns_plot.savefig('output.png')

#求GDP和手機持有率的相關係數
x=select_df["GDP ($ per capita)"]
y=select_df["Phones (per 1000)"]
n=len(x)
x_mean = x.mean()
y_mean = y.mean()
print("資料數:", n)
print("x平均:", x_mean)
print("y平均:", y_mean)
diff = (x-x_mean)*(y-y_mean)
print("x偏差*y偏差和:", diff.sum())
covar = diff.sum()/n
print("共變異數:", covar)
corr = covar/(x.std()*y.std())
print("相關係數:", corr)
print_line()

#資料正規化
from sklearn import preprocessing
df1 = pd.DataFrame({"GDP ($ per capita)" : select_df["GDP ($ per capita)"],
                   "Phones (per 1000)" : select_df["Phones (per 1000)"]})
print(df1.head())
scaler = preprocessing.StandardScaler()
np_std = scaler.fit_transform(df1)
df_std = pd.DataFrame(np_std, columns=["GDP ($ per capita)", "Phones (per 1000)"])
print(df_std.head())
#df_std.head().to_html("Ch13_2_1a_02.html")
df_std.plot(kind="scatter", x="GDP ($ per capita)", y="Phones (per 1000)")

#最小最大值縮放
scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
np_minmax = scaler.fit_transform(df1)
df_minmax = pd.DataFrame(np_minmax, columns=["GDP ($ per capita)", "Phones (per 1000)"])
print(df_minmax.head())
df_minmax.plot(kind="scatter", x="GDP ($ per capita)",y= "Phones (per 1000)")
print_line()

#遺漏值
#採df.dropna()方式，刪除所有橫向 NaN 的記錄(第13行)

#類別值("Region")
label_encoder = preprocessing.LabelEncoder()
select_df["Region"] = label_encoder.fit_transform(select_df["Region"])
#print(select_df) 印出類別值("Region")

#線性回歸
from sklearn.linear_model import LinearRegression
cols = ['Population', 'Area (sq. mi.)', 'GDP ($ per capita)','Phones (per 1000)','Birthrate','Deathrate']
y = select_df["Region"]
lm = LinearRegression()
lm.fit(select_df[cols], y) #cols為要分析的欄位
print("迴歸係數:", lm.coef_)
print("截距:", lm.intercept_ )
coef = pd.DataFrame(select_df[cols].keys(), columns=["features"])
coef["estimatedCoefficients"] = lm.coef_
print(coef)

#MSE
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(select_df['GDP ($ per capita)'], select_df['Phones (per 1000)'])
print(" MSE=",mse)




































