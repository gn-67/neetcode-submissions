class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        numSet = set(nums)
        result = 0

        for num in numSet:
            if num - 1 in numSet:
                continue

            count = 1
            
            while num + 1 in numSet:
                count += 1
                num += 1
            
            result = max(result,count)
        
        return result

        