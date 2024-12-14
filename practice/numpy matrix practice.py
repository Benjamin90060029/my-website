import pandas as pd
idx = ["as","ad","ac"]
data = [1 ,3 ,2]
series = pd.Series(data , index=idx)
series_idx = series.index#取得 series 的索引
series_value =series.values#取得 series 的值（數據）
pineapple = pd.Series([12],index=["pineapple"])
series1 =pd.concat([series,pineapple,pineapple])#將 series 和兩個 pineapple 序列連接起來，產生新序列 series1
series2 = series1.drop("as")#移除as
truefalse = [True, False, True, False]#使用布林列表篩選 series2 的元素
print(series2[truefalse])
print(series1)
