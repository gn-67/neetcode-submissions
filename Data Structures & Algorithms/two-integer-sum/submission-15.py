class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}
        #we use this to store what values we've seen and their index

        for i in range(len(nums)):
            compliment = target - nums[i]

            if compliment in seen:
                return [seen[compliment], i]
            
            else:
                seen[nums[i]] = i
        