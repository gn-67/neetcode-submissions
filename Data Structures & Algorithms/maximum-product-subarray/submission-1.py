class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        result = max(nums)
        minSub = 1
        maxSub = 1

        for number in nums:
            if number == 0:
                minSub = 1
                maxSub = 1
                continue
            
            temp = number * maxSub
            maxSub = max(maxSub * number, minSub * number, number)
            minSub = min(temp, minSub * number, number)
            result = max(result, maxSub)

        return result