class Solution:
    def rob(self, nums: List[int]) -> int:




        def helper(houses):
            rob1 = 0
            rob2 = 0

            for house in houses:
                temp = max(rob1 + house, rob2)
                rob1 = rob2
                rob2 = temp
            
            return rob2
        
        print(nums[0:len(nums) - 1])
        print(nums[1:])

        if len(nums) == 1:
            return nums[0]

        return max(helper(nums[0:len(nums) - 1]), helper(nums[1:]))
        