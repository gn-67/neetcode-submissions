class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            
            if comp in compliment:
                return [compliment[comp], i]

            compliment[nums[i]] = i
        


        