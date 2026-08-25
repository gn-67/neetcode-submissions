class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #we can use a sliding window method
        #we increment while our next character is valid, using a set to track comparisons
        #if we encounter a char we alr seen, we increment the left pointer until our substring is valid again

        maxLen = 0
        left = 0
        right = 0

        if not s:
            return 0
        substring = set()


        while right < len(s):
            while right < len(s) and s[right] in substring:
                substring.remove(s[left])
                left += 1
            substring.add(s[right])
            maxLen = max(maxLen, len(substring))
            right += 1

        
        return maxLen
                

        