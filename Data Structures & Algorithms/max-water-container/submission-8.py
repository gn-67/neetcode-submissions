class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #whenevr we have to use two pointers, its from both ends
        #if they start together, thats more like sliding window


        left = 0
        right = len(heights) - 1
        maxArea = 0


        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            maxArea = max(maxArea, area)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return maxArea

        