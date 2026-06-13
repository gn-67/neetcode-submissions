class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set(nums)
        if len(a) != len(nums):
            return True
        return False
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
        # numset = set(nums)
        # if len(numset) < len(nums):
        #     return True
        # else: return False

        
        