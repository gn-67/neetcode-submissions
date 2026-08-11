class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #we can utilize the two pointer approach to complete this problem in O(n) one pass
        #we can use a global variable to track the max area
        #we can move the pointer pointing to the smaller height forward, because the width is always going to decrease after first area is calculatedd, so we can take a greedy approach and grab the next highest index


        maxArea = 0
        left = 0
        right = len(heights) - 1

        #left cannot be the same as right in this situation
        while left < right:
            print((right - left) * min(heights[left], heights[right]))
            maxArea = max(maxArea, (right - left) * min(heights[left], heights[right]))

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return maxArea

        