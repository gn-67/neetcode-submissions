class Solution:
    def countSubstrings(self, s: str) -> int:
        #so we can start from the middle and treat each substring as if it was starting from the middle
        #if it makes a substring, incremeent count


        count = 0

        for i in range(len(s)):
            left = i
            right = i


            while left >= 0 and right >= 0 and left < len(s) and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            
            left = i
            right = i + 1


            while left >= 0 and right >= 0 and left < len(s) and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        
        return count
        