class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #we shift up whenevr we encounter a negative number

        result = nums[0]
        preSum = 0

        for num in nums:
            if preSum < 0:
                preSum = 0
            preSum = preSum + num

            result = max(result, preSum)

        return result