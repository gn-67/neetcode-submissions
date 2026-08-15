class Solution:
    def longestPalindrome(self, s: str) -> str:

        #we can use a two pointer approach to check the palindrom length of each characecter
        # an easy way to compute this would be to treat each character like the center of a palindromic subtring, then move the pointers outwards to check
        #an edge case we have to consider would be if our string is of even or odd length, because the center would be two different characters and not the same


        result = ""
        resLength = 0

        for i in range(len(s)):
            left = i
            right = i

            while -1 < left and right < len(s) and s[left] == s[right]:
                if right - left + 1 > resLength:
                    result = s[left:right + 1]
                    resLength = right - left + 1 #these are indices
                
                right += 1
                left -= 1

            left = i
            right = i + 1

            while -1 < left and right < len(s) and s[left] == s[right]:
                if right - left + 1 > resLength:
                    result = s[left:right + 1]
                    resLength = right - left + 1 #these are indices
                right += 1
                left -= 1
                
        
        return result



        