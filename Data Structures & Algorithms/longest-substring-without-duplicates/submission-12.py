class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #we can use a two pointer approach
        #we can use a set to track the elements of the curret set
        #if we reach an element that exists in our set, we increment our left pointer until the element isn't present in our set anymore

        #on each iteration, we grab our length and check if its greater than our current max, updating the max as we go

        maxCount = 0
        substring = set()

        left = 0
        right = 0


        while right < len(s):
            while s[right] in substring:
                substring.remove(s[left])
                left += 1
            
            substring.add(s[right])
            maxCount = max(maxCount, right - left + 1)
            right += 1
        
        return maxCount
            
        