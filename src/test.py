import pandas as pd
import pandas_datareader as pds
# Package and modules for importing data; this code may change depending on pandas version
#import pandas.io.data as web
import pandas_datareader.data as web
import datetime
import tushare as ts
import matplotlib.pyplot as plt
#解决画图中文乱码问题
import pylab


import redis
import time
#conn = redis.Redis('18.219.210.244',password='yangguang', port=6379)  # 本机安装，ip为本地地址
#d = ts.get_tick_data('601318',date='2017-06-26')
#print (d);
#conn.set('secret', 'test_1')
#print(conn.get('secret'))
#ts.get_k_data()
#e = ts.get_hist_data('601318',start='2017-06-23',end='2017-06-26')
#print (e);
pylab.mpl.rcParams['font.sans-serif'] = ['SimHei']
pylab.mpl.rcParams['axes.unicode_minus'] = False
#%% 获取中国平安三年内K线数据
ZGPA=ts.get_hist_data('000001')
ZGPA.index=pd.to_datetime(ZGPA.index)

#%% 相关指数
print(ZGPA.tail())
plt.plot(ZGPA['close'],label='收盘价')
plt.plot(ZGPA['ma5'],label='MA5')
plt.plot(ZGPA['ma20'],label='MA20')
plt.legend()
plt.xlabel('日期')
plt.ylabel('股价')
plt.title('中国平安收盘价，MA5，MA20时间序列')

#%% 获取中国平安全部历史数据
ZGPA_all=ts.get_h_data('000001',start='2015-01-01')
ZGPA_all.index=pd.to_datetime(ZGPA_all.index)

#%% 相关指数
print(ZGPA_all.tail())
plt.plot(ZGPA_all['close'],label='收盘价')
plt.legend()
plt.xlabel('日期')
plt.ylabel('股价')
plt.title('中国平安收盘价时间序列(2006至今)')

#%% 计算收益率
ZPGA_Return=((ZGPA_all['close']-ZGPA_all['close'].shift(1))/ZGPA_all \
    ['close'].shift(1)).dropna() #收益率
plt.plot(ZPGA_Return)
print('中国平安的平均日收益率：',ZPGA_Return.mean(),'\n中国平安的收益率标准差：', \
      ZPGA_Return.std())

plt.savefig("filename1.png")
#plt.show()
