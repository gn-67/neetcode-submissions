class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #since we need to keep track of ranges, we can use a sliding window approach here
        #we can use a global variable to track the max profit
        # and we increment the right pointer constantly
        # if we ever reach a point where the price we buy is more than the price we sell, we move the left pointer up to the right,

        buy = 0
        sell = 1

        maxProfit = 0

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                maxProfit = max(maxProfit, prices[sell] - prices[buy])
            elif prices[sell] < prices[buy]:
                buy = sell
                
            sell += 1


        return maxProfit
            


