class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        resLength = 0

        for i in range(len(s)):
            
            #odd strings
            left = i
            right = i
            while -1 < left and len(s) > right and s[left] == s[right]:
                if (right - left) + 1 > resLength:
                    resLength = right - left + 1
                    res = s[left:right + 1]
                
                left -= 1
                right += 1
            
            #even strings
            left = i
            right = i + 1
            while -1 < left and len(s) > right and s[left] == s[right]:
                if (right - left) + 1 > resLength:
                    resLength = right - left + 1
                    res = s[left:right + 1]
                
                left -= 1
                right += 1

        return res
            