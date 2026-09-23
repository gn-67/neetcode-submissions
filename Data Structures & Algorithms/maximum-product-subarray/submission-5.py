class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #we need to track the minimum and maximum of each subarray
        #that way, if we encounter a negative number, we can flip our minimum into maximum
        #if we ever encounter a 0, that resets our progress so we start a new subrarray

        maxSub = 1
        minSub = 1
        result = max(nums)

        for num in nums:
            if num == 0:
                maxSub = 1
                minSub = 1
            
            temp = maxSub * num
            maxSub = max(temp, minSub * num, num)
            minSub = min(temp, minSub * num, num)
            result = max(result, maxSub)

        return result
        