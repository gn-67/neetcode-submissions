class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #array gives us two sorted halves

        start_i, end_i = 0, len(nums) - 1

        while start_i <= end_i:
            middle = (start_i + end_i) // 2

            if nums[middle] == target:
                return middle

            #left sorted portion
            if nums[start_i] <= nums[middle]: #this means we are in the left side sorted

                if target > nums[middle] or target < nums[start_i]: #if the largest value in our range
                    start_i = middle + 1
                else:
                    end_i = middle - 1

            else:
                if target < nums[middle] or target > nums[end_i]:
                    end_i = middle - 1
                else:
                    start_i = middle + 1


        return -1

        
        #   while start_i <= end_i:
        #     if nums[start_i] < nums[end_i]: #no matter what, if it has been rotated the left value should be greater than right
        #         result = min(result, nums[start_i])
        #         break

        #     middle = (start_i + end_i) // 2
        #     result = min(result, nums[middle])

        #     if nums[middle] >= nums[start_i]: # this means the smaller sorted side is to the right of the middle
        #         start_i = middle + 1
        #     else: 
        #         end_i = middle - 1 # smaller sorted side is to the left
            
        
        # return result