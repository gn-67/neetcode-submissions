class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #we cam take a greedyt approach
        #where we calculate our current subarray by summing elements before and adding current element in iteratoin
        #howevger if our current sum before the current element is negative, we reset the sum back to 0 because adding to a negative is less than a positive sum

        #on each iteration, we checkj our current sum against our maxsub and update it accordingly


        curSub = 0
        maxSub = nums[0]

        for num in nums:
            if curSub < 0:
                curSub = 0
            
            curSub += num
            maxSub = max(maxSub, curSub)
        

        return maxSub
        