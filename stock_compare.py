#### 功能:将多个股票放在同一图表中进行比较 #####
#### 调用股票数据接口 tushare
import tushare as ts
import pandas as pd # 数据分析库
import numpy as np  # 数学计算基础库
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签


def draw(codes, count) :
    index = 0
    for key, value in codes.items() :
        data = ts.get_hist_data(key)  #从tushare上获得股市行情数据
        data = data.head(count)
        data = data.sort_index(ascending=True) #排序

        data = data[['close']]
        data = data.rename(columns={'close':value}) #重命名列名
        if index == 0 : 
            all_data  = data
            index += 1
            continue 
        all_data = all_data.join(data) #叠加多个股票信息
    all_data = all_data.apply(lambda x: x / x[-1]) #数据归整到同一个坐标中
    all_data = all_data.fillna(0) #空值填充为0
    all_data.plot(figsize=(15,10)) #放大图表
    plt.show()
    
draw({'600460': u'士兰微', '002049':u'紫光国芯' }, 100)
