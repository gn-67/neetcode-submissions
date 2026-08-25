class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #we can use a single pointer and iterate through

        i = 0
        result = 0
        while i < len(nums):
            count = 0
            while i < len(nums) and nums[i] == 1:
                count += 1
                i += 1
            result = max(result, count)
            i += 1
        return result
        