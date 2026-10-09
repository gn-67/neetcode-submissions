class Solution:
    def canJump(self, nums: List[int]) -> bool:

        #maybe we can look at this from the reverse
        #we can check to see if the jump distance of each index is able to reach the end, and if it does we can move our goal up from the end to the next available index

        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= goal:
                goal = i
            
        if goal == 0:
            return True
        
        return False
        