import re

class Solution:
    def isPalindrome(self, s: str) -> bool:


        string = re.sub(r"[^A-Za-z0-9]", "", s,)
        nstring = string.lower()

        left, right = 0, len(nstring) - 1

        while left <= right:
            if nstring[left] != nstring[right]:
                return False
            else:
                left += 1
                right -= 1
        
        return True
        