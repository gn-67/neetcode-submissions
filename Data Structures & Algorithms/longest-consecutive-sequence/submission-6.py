class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #we can create a set for hte elements for o(1) lookup
        # we can check each element, see if one before it exists, 
        # and if it doesn't we check the next value, keep counts

        maxlen = 0

        numset = set(nums)

        for i in range(len(nums)):
            cur = nums[i]
            if cur - 1 in numset:
                continue

            length = 1
            
            while cur + 1 in numset:
                length += 1
                cur += 1
            
            maxlen = max(maxlen, length)
        
        return maxlen

        