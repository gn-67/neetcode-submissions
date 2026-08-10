class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        dictT = {}
        dictS = {}

        for i in range(len(s)):
            if t[i] in dictT:
                dictT[t[i]] += 1
            elif t[i] not in dictT:
                dictT[t[i]] = 1
            if s[i] in dictS:
                dictS[s[i]] += 1
            elif s[i] not in dictS:
                dictS[s[i]] = 1
        
        if dictT != dictS:
            return False
        
        return True
