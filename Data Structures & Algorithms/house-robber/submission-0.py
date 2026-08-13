class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0

        for number in nums:
            temp = max(rob1 + number, rob2) #we rob rob2, OR we decide to go with the one before
            rob1 = rob2
            rob2 = temp 
        
        return rob2

        