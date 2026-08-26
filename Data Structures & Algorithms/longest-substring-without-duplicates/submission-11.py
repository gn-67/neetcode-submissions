class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window approach
        #set for cur substring O(1)
        #rihgt -> char not in substring
        #left _> until char not in substring -> right pointer


        sub = set()
        result = 0

        left = 0
        right = 0

        while right < len(s):
            while s[right] in sub:
                sub.remove(s[left])
                left += 1
            
            sub.add(s[right])
            result = max(result, len(sub))
            right += 1
        
        return result

        #zxzy
        #{xzy} result = 3 right = 3 left = 1
        

        