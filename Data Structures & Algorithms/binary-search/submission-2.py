class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            middle = start + (end - start) // 2
            if target < nums[middle]:
                end = middle - 1
            elif target > nums[middle]:
                start = middle + 1
            elif target == nums[middle]:
                return middle
        
        return -1







        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # begin_i = 0
        # end_i = len(nums) - 1

        # while begin_i <= end_i:
        #     midpoint = begin_i + (end_i - begin_i) // 2
        #     midpoint_value = nums[midpoint]
        #     if midpoint_value == target:
        #         return midpoint

        #     elif target < midpoint_value: #item we are looking for is to the left of midpoint
        #         end_i = midpoint - 1

        #     elif target > midpoint_value:  #item is greater than mid value, we start at the right
        #         begin_i = midpoint + 1

        # return -1

        