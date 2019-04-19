stocks = float(input('please enter amount of stocks bought:')) #2,000
amount_per_stock = float(input('please enter amount per stock:')) #40.00
print('AMOUNT BOUGHT:\t$', format(stocks * amount_per_stock,',''.2f' ))

brokerGets = float(input('please enter amount broker gets from stocks')) #3 percent
print('BROKER GETS:\t$', format(stocks * (amount_per_stock)*brokerGets,',''.2f'))

StocksSold =float(input('amount of stocks sold:')) #2000
stocksSoldfor=float(input('each stock sold for:')) #42.75
print('AMOUNT JOE SOLD:\t$', format(StocksSold * stocksSoldfor,',''.2f' ))

BrokerGetsFromSales=float(input('please enter amount broker gets from stcoks sold:')) #3 percent
print('BROKER GETS:\t$',format(StocksSold*stocksSoldfor*BrokerGetsFromSales,',''.2f'))

profit= float(input('please enter profit before payment to broker:')) #5,500
print('Overall profit after broker payments:\t$',format(profit-(stocks * (amount_per_stock)*brokerGets)-(StocksSold*stocksSoldfor*BrokerGetsFromSales),',''.2f', ))

if profit >=0:
    print ('you made profit!')
else:
    print('you did not make a profit')


