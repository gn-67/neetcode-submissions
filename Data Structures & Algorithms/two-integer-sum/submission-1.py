class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdict = {}
        for i in range(len(nums)):
            if target - nums[i] in numdict: 
                return [numdict[target - nums[i]], i]
            else:
                numdict[nums[i]] = i 



# loop through list nums
#