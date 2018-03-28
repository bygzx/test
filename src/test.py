import pandas as pd
import pandas_datareader as pds
# Package and modules for importing data; this code may change depending on pandas version
#import pandas.io.data as web
import pandas_datareader.data as web
import datetime
import tushare as ts
import redis
import time
conn = redis.Redis('18.219.210.244',password='yangguang', port=6379)  # 本机安装，ip为本地地址
#d = ts.get_tick_data('601318',date='2017-06-26')
#print (d);
conn.set('secret', 'test_1')
print(conn.get('secret'))
#ts.get_k_data()
#e = ts.get_hist_data('601318',start='2017-06-23',end='2017-06-26')
#print (e);
