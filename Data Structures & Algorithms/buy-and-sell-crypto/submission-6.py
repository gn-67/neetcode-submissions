class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell = 0, 1 #you cant buy and sell same day, you cant sell before u buy
        mProfit = 0
        while sell < len(prices):

            if prices[sell] < prices[buy]:
                buy = sell
                sell += 1
                continue


            if prices[sell] >= prices[buy]:
                profit = prices[sell] - prices[buy]
                if profit > mProfit:
                    mProfit = profit
                sell += 1
                continue

        
        return mProfit




        
        