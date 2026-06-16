class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        left, right = 0, 1

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
                right += 1
                continue
            else:
                print(prices[right] - prices[left])
                maxP = max(maxP, (prices[right] - prices[left]))
                right += 1
        
        return maxP


        
        