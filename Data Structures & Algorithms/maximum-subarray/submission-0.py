class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSub = 0

        for num in nums:
            if curSub < 0:
                curSub = 0
            curSub += num
            maxSub = max(maxSub, curSub)
        
        return maxSub
        