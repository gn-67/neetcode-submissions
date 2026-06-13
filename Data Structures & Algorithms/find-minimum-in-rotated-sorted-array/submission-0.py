# we search for the lowest value in array, get its position, then calculate the rotations from there 
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        return min(nums)
        # start_i = 0
        # end_i = n - 1
        # target_i = 0

        # while start_i <= end_i:
        #     middle = start_i + (end_i - start_i) // 2
        #     if target < nums[middle]:
        #         end_i = middle - 1
        #     elif target > nums[middle]:
        #         start_i = middle + 1
        #     elif target == nums[middle]:
        #         target_i = middle
        


        