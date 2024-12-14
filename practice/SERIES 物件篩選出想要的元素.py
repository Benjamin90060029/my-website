import  pandas as pd
index = ['pen','eraser','cup','grape']
data = [4, 3,45,57 ]
data2 = [8,24,22,96]
series = pd.Series(data , index=index)
series2 = pd.Series(data2 , index=index)
data3 = {"fruit":['grape', 'apple', 'strewberry'],"time":[1, 4, 5],"year":['2001','1855','2011']}
#series1 = series[series<4][series>2]
item = series.sort_index()
item = series.sort_values()
df = pd.DataFrame([item, series2])
df2 = pd.DataFrame(data3)
df3 = pd.DataFrame()
df.index = [2,3]#改變行INDEX的名稱
df2.columns =['fruit2','time','year']#改變列的欄位名稱
series3 =pd.Series(["mango",5,'2008'], index= ["fruit2", "time", "year"])
df2 = df2._append(series3, ignore_index=True)
df2["price"] = [27, 30, 45, 18]
new_column = pd.Series(['10/17', '1/1', '2/3', '8/15'], index=[-1, 0, 1, 2])
df2["date"] = new_column
df2.index = [-1, 0, 1, 2]
df2loc = df2.loc[[0, 1 ],["fruit2", "time", "year"]]#將行列交集的部分取出
print(df)
print(df2)
print(df2loc)