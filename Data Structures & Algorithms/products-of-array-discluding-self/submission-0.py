class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #brute force solution
        result = []
        for i in range(len(nums)):
            k = 1
            for j in range(len(nums)):
                if j != i:
                    k = nums[j] * k
            result.append(k)
        
        return result
            