class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #we can use a sliding window approach, updating our maxProfit
        #whenever we encounter a new day where we are selling for less than we buy, we should update our buy pointer to that
        #otherwise we keep iterating, updating our max profit

        maxProfit = 0

        buy = 0
        sell = 1

        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
            
            profit = prices[sell] - prices[buy]
            maxProfit = max(maxProfit, profit)

            sell += 1
        
        return maxProfit


