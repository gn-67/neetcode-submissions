class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #its optimal to replace the character that is most. frequent in the substring

        counts = collections.defaultdict(int) #defualts all values to 0
        result = 0  
        left = 0
        right = 0

        #AABB k = 1

        while right < len(s):
            counts[s[right]] += 1

            while right - left + 1 - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
            right += 1
        
        return result
        