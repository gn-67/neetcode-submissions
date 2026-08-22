class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #we can take a greedy two pointer approach here
        #we can use a global variable to track our max area, and update it accordingly on each iteration
        #each time, we move the pointer on the smaller height forward, in hopes of meeting a taller height and increasing our area as we decrease our width


        left = 0
        right = len(heights) - 1
        maxArea = 0

        while left < right:
            area = (right - left) * (min(heights[left],heights[right]))
            maxArea = max(maxArea, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return maxArea
