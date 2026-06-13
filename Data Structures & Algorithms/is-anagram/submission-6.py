class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in d1:
                d1[s[i]] += 1
            if s[i] not in d1:
                d1[s[i]] = 1
            if t[i] in d2:
                d2[t[i]] += 1
            if t[i] not in d2:
                d2[t[i]] = 1


        if d1 == d2:
            return True
        else: return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        













        
        
        
        # if len(s) != len(t):
        #     return False
        # else:
        #     set(s)
        #     set(t)
        #     if sorted(set(s)) != sorted(set(t)):
        #         return False
        # return True
        