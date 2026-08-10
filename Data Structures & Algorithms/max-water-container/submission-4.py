class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0


        # we move only the pointer at the smaller height
        # we can safely discard the smaller height as the width will only get smaller no matter what, so we have to optimize for the potential max height

        while left < right:
            maxArea = max(maxArea, ((right - left) * min(heights[left],heights[right])))

            if heights[left] < heights[right]:
                left += 1

            else:
                right -= 1




        
        return maxArea



        