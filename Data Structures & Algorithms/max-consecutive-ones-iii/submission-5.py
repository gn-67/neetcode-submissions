class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        maxLen = 0
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
            

            maxLen = max(right - left + 1, maxLen)
            right += 1
        
        return maxLen
            


        