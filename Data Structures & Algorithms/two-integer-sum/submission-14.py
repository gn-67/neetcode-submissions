class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}
        #we use this to store what values we've seen and their index

        for i in range(len(nums)):
            

            if target - nums[i] in seen:
                return [seen[target - nums[i]], i]
            
            else:
                seen[nums[i]] = i
        