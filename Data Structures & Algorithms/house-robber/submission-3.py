class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0

        #rob2 is the last house we robbed
        #rob1 is the house before that

        for house in nums:
            temp = max(house + rob1, rob2)
            #we either skip the house before, or we stay at just that one
            rob1 = rob2
            rob2 = temp
        
        return rob2