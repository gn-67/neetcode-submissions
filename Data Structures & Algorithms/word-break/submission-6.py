class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        #we can use dynamic programming here to build our solution
        #we can work bottom up
        #we can use a cache of size s storing each index in the string
        #and we can have it be true if at the index there is a word from dict that fits between index and the end of the string
        #if we index backwards, we could probably match each subset of indices to a word in dict, and if 



        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        #our base case, if we can reach this then its green

        for i in range(len(s) -1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if dp[i] == True:
                    break
            
        return dp[0]

        