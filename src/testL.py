# from CAL.PyCAL import Date
#
# start = '2010-01-01'                       # 回测起始时间
# end = '2015-05-05'                         # 回测结束时间
# benchmark = 'HS300'                        # 策略参考标准
# universe = set_universe('HS300')               # 证券池，支持股票和基金
# capital_base = 1000000                      # 起始资金
# longest_history = 0                        # handle_data 函数中可以使用的历史数据最长窗口长度
# refresh_rate = 1                          # 调仓频率，即每 refresh_rate 个交易日执行一次 handle_data() 函数
# longest_history = 1
#
#
# def initialize(account):                   # 初始化虚拟账户状态
#     account.isBuyPeriod = False
#     account.dayCount = 0
#
# def handle_data(account):                  # 每个交易日的买入卖出指令
#     account.dayCount += 1
#     if account.isBuyPeriod:                # 每60个工作日（3个月）调仓
#         hist = account.get_history(longest_history)
#         endDate = Date.fromDateTime(account.current_date)
#         startDate = endDate - 30
#         res =  DataAPI.NewsSentimentIndexGet(secID=account.universe, field=['secID', 'newsPublishDate', 'sentimentIndex'], beginDate=startDate.strftime('%Y%m%d'),endDate=endDate.strftime('%Y%m%d'))
#         res = res.groupby('secID')
#
#         # top 10%
#         top10 = res.mean().sort('sentimentIndex', ascending=False).head(int(0.1*len(res)))
#         buyList = list(top10.index)
#         print u"%s 买入 : %s" % (endDate, buyList)
#
#         # 等权重买入
#         if len(buyList) != 0:
#             singleCash = account.cash / len(buyList)
#             for stock in buyList:
#                 approximationAmount = int(singleCash / hist[stock]['closePrice'][-1]/100.0) * 100
#                 order(stock, approximationAmount)
#
#         account.isBuyPeriod = False
#         account.dayCount = 0
#     elif account.dayCount == 59:          # 调仓日前一日清空当前仓位
#         for stock in account.valid_secpos:
#             order_to(stock,0)
#         account.isBuyPeriod = True