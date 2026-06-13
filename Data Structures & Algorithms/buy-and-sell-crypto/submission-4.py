#two pointers, one buy and one sell
# if the left pointer(buy) is less than sell, leave the left pointer there

# if n+1 is < n, move sell to n + 1. if n + 2 > n, we have our sellDay
# at the end subtract sell from buy and return total, return 0 elsewhise
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left, right = 0, 1 
        
        while right < len(prices):
            sell = prices[right]
            buy = prices[left] #we have to buy before we sell
            
            if sell > buy:
                cur_profit = sell - buy
                if cur_profit > max_profit:
                    max_profit = cur_profit

            elif sell < buy:
                left = right #BECAUSWE we found a new low price
            
            right += 1 #do this at END of cycle
                

        if max_profit > 0:
            return max_profit
        else:
            return 0


def stringCheck(input): 
    s = input.split("--")
    if len(s) != 5:
        return false


