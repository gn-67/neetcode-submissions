# start with two pointers one on each end and have htem iterate inwhile checking each character
#verify edge cases like empty 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        s = s.lower()
        while left <= right:
            if s[left].isalnum() == False:
                left += 1
                continue
            elif s[right].isalnum() == False:
                right -= 1
                continue
            if s[left] != s[right]:
                return False
            else:
                left +=1
                right -=1
                continue
        return True