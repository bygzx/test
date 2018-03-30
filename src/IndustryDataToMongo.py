#股票列表
from pymongo import MongoClient
import tushare as ts
import datetime
import json

s = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S');
print ('开始时间：'+s)

conn = MongoClient('18.219.210.244', port=27017)
db = conn.mydb
db.authenticate("root", "123456")
#连接表
collection = db.myset


#查看全部表名称
# db.collection_names()
#df = ts.get_stock_basics()
df = ts.get_cashflow_data(2017,3)
jsonS = json.loads(df.to_json(orient='records'))
# s1 = db.tickbasicsdata.find({"name":"渝开发"},{"name":1});
# if not s1 or s1.count() == 0:
#     print("result is null")
# else:
#     print(len(s1));
# print(len(jsonS));
for json in jsonS:
    print(json["name"]);
    # s1 = db.tickbasicsdata.find({"name":json["name"]},{"name":1}).count();
    # print(s1);
    j = db.tickbasicsdata.find({"name":json["name"]},{"name":1});
    if not j or j.count() == 0:
     print(str(json["name"])+"：没数据");
    else:
        print(str(j[0]["name"])+":"+str(j[0]["_id"]));
        db.tickbasicsdata.update({"name" : str(j[0]["name"])},{"$set" : {"code" : json["code"]}});
# #db.tickbasicsdata.insert(json.loads(df.to_json(orient='records')));
# print ('开始时间：'+s)
# print ('结束时间：'+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# db.tickbasicsdata.update({"name" :"太平洋"},{"$set" : {"code" : "600929"}});
