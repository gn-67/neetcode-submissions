class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(houses):
            house1 = 0
            house2 = 0


            for house in houses:
                temp = max(house1 + house, house2)
                house1 = house2
                house2 = temp

            return house2

        
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
        