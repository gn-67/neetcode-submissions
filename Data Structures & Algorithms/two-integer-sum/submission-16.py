class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # nums[i] + nums[j] == target
        # i, j
        #nums[j] == target - nums[i]
        #complient 
        #hashmap

        seen = {}

        for i in range(len(nums)):
            compliment = target - nums[i]

            if compliment in seen:
                return [seen[compliment], i]
            
            seen[nums[i]] = i
        

        