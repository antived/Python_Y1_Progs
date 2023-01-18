# AdAstra 2022-23 problem-4
#
# program to maximize_profit from day trading over N days, given N days worth
# of stock price projection of a stock. this takes a simplisitic, short-sighted
# view (that of "day trader") and not that of a long-term equity-investor. the
# main assumtion in day-trading is that you buy when price is showing a trend
# of increasing price and sell when price is showing a trend of decreasing price
# However, a long term equity-investor holds stocks over longer period of time
# and does not trade daily on increasing/decreasing price trends.
#
# - vedant dutta

def maximize_profit(stockPriceArr):
    maxProfit = 0      # initially my profit is zero as I've sold nothing
    stocksInHand = 0    # start with zero stocks-in-hand
    
    # run thru stockPriceArr (projections) to determine ideal action to perform
    # on each day, based on the stock price trend (increasing or decreasing)
    for i in range(1, len(stockPriceArr)):
        # price increasing, so buy 1 stock (max you can buy as per problem-4)
        if (stockPriceArr[i] > stockPriceArr[i-1]):
            stocksInHand = stocksInHand + 1
        # price decreasing and stocksInHand > 0, then sell all stocksInHand !
        elif (stockPriceArr[i] < stockPriceArr[i-1]) and (stocksInHand > 0):
            stockPriceDiff = stockPriceArr[i-1] - stockPriceArr[i]
            maxProfit = maxProfit + (stocksInHand * stockPriceDiff)
            stocksInHand = 0    # all stocks sold
            
    # on last day of trading, if stocksInHand > 0, we shall sell them for 
    # the last price (even if this is a loss making propition).
    # note that this logic is added later, because without this, my results
    # were not tallying with problem-4 expected results.
    # the rationale for this could be that a day-trader must exit the stock
    # compeltely at the end of the trading term, and maximize whatever profit
    # they can (which doesn't happen if they still hold on to some stocks).
    if stocksInHand > 0:
        stockPriceDiff = stockPriceArr[-1] - stockPriceArr[-2]
        maxProfit = maxProfit + (stocksInHand * stockPriceDiff)
        
    # Return the maximum profit
    return maxProfit

# main()

# invoke the function with various test arrays of price projections
#
prices = [1, 3, 1, 2]           # expected value is 3 as per problem given
print(maximize_profit(prices))

prices = [3, 4]                 # expected value is 1 as per problem given
print(maximize_profit(prices)) 

prices = [4, 3]                 # expected value is 0 as per problem given
print(maximize_profit(prices)) 

prices = [1, 2, 100]            # expected value is 197 as per problem given
print(maximize_profit(prices))

prices = [5, 3, 2]              # expected value is 0 as per problem given
print(maximize_profit(prices))
