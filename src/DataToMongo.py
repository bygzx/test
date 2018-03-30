import pymongo
from pymongo import MongoClient
import datetime
import json
import tushare as ts
conn = MongoClient('18.219.210.244', port=27017)
db = conn.mydb
db.authenticate("root", "123456")
#连接表
collection = db.myset


#查看全部表名称
db.collection_names()

# df = ts.get_k_data('601318',start='2017-06-23',end='2017-06-26')
# print(1);
# df = ts.get_k_data('601989',ktype='W') #2007-03-02
# print(df);
# if df.empty != True:
#     jsonS = json.loads(df.to_json(orient='records'));
#     # print(jsonS);
#     print(1);
#     print(len(jsonS));
    # db.tickdata.insert(json.loads(df.to_json(orient='records')));

# db.tickdata.insert(json.loads(df.to_json(orient='records')));
s = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S');
print ('开始时间：'+s)

n=1000
count=0
countx=0
while n<1000:
    n+=1;
    x=str(n);
    #6位补0
    a = x.zfill(6)
    # print(x+':'+str(len(x))+':'+a);
    df = ts.get_k_data(a,ktype='W')
    if df.empty != True:
        countx+=1
        jsonS = json.loads(df.to_json(orient='records'))
        count+=len(jsonS);
        print(a+"不是空的,长度："+str(len(jsonS)));
        #print(a+"长度："+str(len(jsonS)));
        db.tickdata.insert(json.loads(df.to_json(orient='records')));
print ('开始时间：'+s)
print ('结束时间：'+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print("总票数："+str(countx)+"总数据量："+str(count))
#     else:
#         print(a+"是空的");
# print(df);
# print(json.loads(df.to_json(orient='records')));
# jsonS = json.loads(df.to_json(orient='records'));
# # print(jsonS[1]);
# x=0;
# for i in jsonS:
#     x+=1;
    # i['name']='601318';
# if x>0:
#     db.tickdata.insert(json.loads(df.to_json(orient='records')));