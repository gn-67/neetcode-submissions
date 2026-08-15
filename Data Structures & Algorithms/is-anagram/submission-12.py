class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}

        if len(s) != len(t):
            return False

        
        for i in range(len(s)):
            if s[i] in countS:
                countS[s[i]] += 1
            else:
                countS[s[i]] = 1


            if t[i] in countT:
                countT[t[i]] += 1
            else:
                countT[t[i]] = 1


        if countS != countT:
            return False

        return True

        