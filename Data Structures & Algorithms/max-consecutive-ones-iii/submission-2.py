class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #we can use a sliding window approach here
        #we can use a global result variable
        #and have our left pointer always hsorten the window, while our right pointer expands it
        #we can also keep a count of the number of 0s in our interval,
        #if that number exceeds K then we can start shortening our window


        result = 0
        count = 0

        left = 0
        right = 0

        while right < len(nums):
            if nums[right] == 0:
                count += 1
            while count > k:
                if nums[left] == 0:
                    count -= 1
                left += 1
            right += 1
            result = max(result, right - left)
        
        return result
            



        