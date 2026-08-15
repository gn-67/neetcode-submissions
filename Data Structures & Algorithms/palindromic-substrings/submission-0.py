class Solution:
    def countSubstrings(self, s: str) -> int:

        #we can use a two pointer approach, treat each character as the middle value and iterate out
        #use a local variable to count up each time its a valid palindrome
        #we need a way to track which 

        count = 0

        for i in range(len(s)):
            left = i
            right = i

            while -1 < left and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            

            left = i
            right = i + 1

            while -1 < left and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            
        
        print(count)
        return count