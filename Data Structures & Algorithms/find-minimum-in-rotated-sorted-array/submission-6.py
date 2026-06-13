# we search for the lowest value in array, get its position, then calculate the rotations from there 
class Solution:
    def findMin(self, nums: List[int]) -> int:
        #left side of sorted array will always be greater
        result = nums[0]
        start_i, end_i = 0, len(nums) - 1

        while start_i <= end_i:
            if nums[start_i] < nums[end_i]: #then we are in the smaller sorted array
                result = min(result, nums[start_i])

            middle = (start_i + end_i) // 2
            result = min(result, nums[middle])

            if nums[middle] >= nums[start_i]:
                start_i = middle + 1

            else: 
                end_i = middle - 1


        return result
            



























        # result = nums[0]
        # start_i = 0
        # end_i = len(nums) - 1

        # while start_i <= end_i:
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
        


        