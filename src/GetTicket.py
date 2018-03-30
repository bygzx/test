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
#codeList = db.tickdata.find({},{"code":1});
codeList = db.tickdata.distinct('code');
print(codeList);
#db.collectionName.distinct('trnrec.stunum', {"trnrec.rttype":0,"trnrec.createtime":{ $gte: ISODate("2017-11-23T00:00:00+0800"), $lt: ISODate("2017-11-24T00:00:00+0800")}}).length
#db.tickdata.insert(json.loads(df.to_json(orient='records')));