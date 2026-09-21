class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #we need special treatment for negative numbers
        #we should proceed by calculating the minimum AND maximum


        result = max(nums)
        curMax = 1
        curMin = 1

        for num in nums:
            if num == 0:
                curMax = 0
                curMin = 0
            
            temp = curMax * num
            curMax = max(curMax * num, curMin * num, num)
            curMin  = min(temp, curMin * num, num)
            result = max(curMax, result)
        
        return result
                
        