import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #we have to check that the left pointer is equal to right pointer

        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        print(s)

        L = 0
        R = len(s) - 1

        while L < R:
            if s[L] != s[R]:
                return False
            else:
                L += 1
                R -= 1
        
        return True
            
        