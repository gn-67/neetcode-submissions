class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #we can use a sliding window approach while building up our string until we reach a duplicate value
        #wait theres a more efficient way
        #if we encounter a value that isn't in the start, we move our start pointer up and thats it 
        if len(s) == 0:
            return 0
        left = 0
        right = 1
        string = set(s[left])

        maxLen = 0

        while left < len(s):
            while right < len(s) and s[right] not in string:
                string.add(s[right])
                right += 1
            maxLen = max(maxLen, len(string))
            string.remove(s[left])
            left += 1

        
        return maxLen



