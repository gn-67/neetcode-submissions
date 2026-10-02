class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        #we can use a global variable to check length and update it accordingly
        #it is optimate to replace the character that is most frequent in the substring

        counts = collections.defaultdict(int) #defaults all values to 0 

        maxLen = 0
        right = 0
        left = 0


        while right < len(s):
            counts[s[right]] += 1

            while (right - left + 1) - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1
            
            maxLen = max(right - left + 1, maxLen)
            right += 1
        
        return maxLen
        