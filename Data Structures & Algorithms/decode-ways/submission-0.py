class Solution:
    def numDecodings(self, s: str) -> int:
        #we check each sequence of chars
        # they could all be individual or groups of two
        # I will use a recursive cache approach

        #first lets create our cache

        dp = {len(s) : 1}
        #our base case, our last element can only create one element

        def dfs(i):
            if i in dp:
                return dp[i]
            
            if s[i] == "0":
                return 0
            
            result = dfs(i + 1)

            if (i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"))):
                result += dfs(i+2)
            
            dp[i] = result
            return result


        return dfs(0)
        