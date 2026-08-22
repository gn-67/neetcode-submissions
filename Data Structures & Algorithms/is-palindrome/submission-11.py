import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        #first we should normalize the string so we can accurately compare both ends using a two pointer approach
        string = s.lower().replace(" ", "")
        string = re.sub(r'[^A-Za-z0-9]', "", string)

        left = 0
        right = len(string) - 1

        while left <= right:
            if string[left] != string[right]:
                return False
            
            left += 1
            right -= 1
        
        return True

        