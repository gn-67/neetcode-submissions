#lets search by the compliment

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set() #use a set for o(1) lookup
        
        for i in range(len(nums)):
            comp = target - nums[i]

            if comp in seen:
                return [nums.index(comp), i]
            
            seen.add(nums[i])

        