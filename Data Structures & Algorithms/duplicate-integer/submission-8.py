class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unums = set(nums)
        if len(nums) != len(unums):
            return True
        return False

        