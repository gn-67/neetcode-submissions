class Solution:
    def longestPalindrome(self, s: str) -> str:
        #we have to expand out from the each char
        #treating it like the middle of a palindrome

        result = ""
        curLen = 0



        for i in range(len(s)):
            left = i
            right = i

            while left >= 0 and left < len(s) and right >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > curLen:
                    curLen = right - left + 1
                    result = s[left:right + 1]
                right += 1
                left -= 1
            
            
            left = i
            right = i + 1
            while left >= 0 and left < len(s) and right >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > curLen:
                    curLen = right - left + 1
                    result = s[left:right + 1]
                right += 1
                left -= 1
            

        
        return result
                
        