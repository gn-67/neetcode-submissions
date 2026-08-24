class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        #sliding window greedy
        #we keep flipping the 0s into ones until we are all out of 0's
        #then we record the length of our string as a max and iterate the left pointer up to the next 0
        #then we repeat, increment until we at our max 0, grab the length


        result = 0
        numZeros = 0
        left = 0
        right = 0

        while right < len(nums):
            if nums[right] == 0:
                    numZeros += 1

            
            while numZeros > k:
                if nums[left] == 0:
                    numZeros -= 1
                left += 1


            result = max(result, right - left + 1)
            right += 1

        return result 
            
        