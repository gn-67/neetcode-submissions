class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxlen = 0
        
        for i in range(len(nums)):
            result = []
            k = 1
            if nums[i] - k not in numset:
                result.append(nums[i])
                while nums[i] + k in numset:
                    result.append(nums[i] + k)
                    k += 1
            if len(result) > maxlen:
                maxlen = len(result)
            

        return maxlen


