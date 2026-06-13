class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        scount = {}
        tcount = {}
        
        for i in range(len(s)):
            if s[i] in scount:
                scount[s[i]] += 1
            elif s[i] not in scount:
                scount[s[i]] = 1
            
            if t[i] in tcount:
                tcount[t[i]] += 1
            elif t[i] not in tcount:
                tcount[t[i]] = 1
        
        if scount != tcount:
            return False
        return True
        