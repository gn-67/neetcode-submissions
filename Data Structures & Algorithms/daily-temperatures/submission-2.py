class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #whenver we need a next greater element or next smaller element -> monotonic stack

        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                stackTemp, stackI = stack.pop()
                result[stackI] = i - stackI
            
            stack.append([temp, i])
        
        return result

        