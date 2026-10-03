class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        length = 0
        counts = collections.defaultdict(int)

        left = 0
        right = 0

        while right < len(s):
            counts[s[right]] += 1

            if (right - left + 1) - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1
            
            length = max(length, right - left + 1)
            right += 1
        
        return length

        