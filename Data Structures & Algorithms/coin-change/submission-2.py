class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #we can utilize a bottom up approach using a cache
        DP = [amount + 1] * (amount + 1) #this contains amount of coins to build the amount

        DP[0] = 0

        for a in range(1, amount + 1):
            #we try each coin to build the amount
            for coin in coins:
                if a - coin >= 0:
                    DP[a] = min(DP[a], 1 + DP[a-coin])
        
        if DP[amount] != amount + 1:
            return DP[amount]
        
        return -1

