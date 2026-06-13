class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        maxA = 0

        while left < right:
            if heights[left] <= heights[right]:
                area = (right - left) * heights[left]
                left += 1
            
            elif heights[right] < heights[left]:
                area = (right - left) * heights[right]
                right -= 1

            if area > maxA:
                maxA = area
            
        return maxA





























        # maxA = 0
        # left, right = 0, len(heights)-1

        # while left < right:
        #     if heights[left] <= heights[right]:
        #         area = (right - left) * heights[left]
        #         left += 1
        #     elif heights[left] > heights[right]:
        #         area = (right - left) * heights[right]
        #         right -= 1

        #     if area > maxA:
        #         maxA = area

        # return maxA

            

        