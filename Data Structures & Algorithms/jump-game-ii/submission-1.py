class Solution:
    def jump(self, nums: List[int]) -> int:
        #we can use a greedy approach here
        #we can use a left and right pointer, where our right pointer points to the furthest index we can reach
        #on each pass, we iterate through and find the new furthest, and increment numebr of jumps

        jumps = 0
        right = 0
        left = 0

        while right < len(nums) - 1:
            jumps += 1
            furthest = 0
            for i in range(left, right + 1):
                furthest = max(furthest, i + nums[i])
            left = right + 1
            right = furthest
        
        return jumps


        