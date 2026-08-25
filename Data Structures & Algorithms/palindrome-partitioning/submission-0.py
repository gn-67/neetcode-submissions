class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #the two decisions here is we either parition the string, or we can continue

        partition = []
        result = []

        def isPali(l,r,s):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i):
            if i >= len(s):
                result.append(partition.copy())
                return
            
            for j in range(i, len(s)):
                if isPali(i, j, s):
                    partition.append(s[i:j+1])
                    dfs(j+1)
                    partition.pop()
            
        dfs(0)
        return result

  